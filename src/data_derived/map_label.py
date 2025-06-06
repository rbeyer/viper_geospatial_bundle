#!/usr/bin/env python
"""
This program runs gdal_translate to produce a draft XML label and a GeoTIFF,
and then gathers information, and produces a modified label.
"""

import argparse
from datetime import date, datetime, timezone
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET

from osgeo import gdal
import pandas as pd
import yaml

from vipersci.pds.datetime import isozformat
from vipersci.pds.labelmaker import vid_max, write_xml
from vipersci.pds.xml import find_text, ns


def arg_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument(
        "-c",
        "--csv",
        help="The csv file of LROC LIDVIDS to read for orthoimage labels.",
    )
    parser.add_argument("-o", "--output", type=Path, help="Output XML label file.")
    parser.add_argument(
        "-p", "--projection", help="A .prj file with a WKT string.", default="viper.prj"
    )
    parser.add_argument(
        "-t", "--template", type=Path, help="XML template to use to create the output."
    )
    parser.add_argument("-y", "--yaml", type=Path, help="The YAML file to load.")
    parser.add_argument("input", type=Path, help="Input GeoTIFF data.")

    return parser


def get_lv(path, product_id):
    df = pd.read_csv(path, names=["reference_type", "lidvid"])
    row = df[df["lidvid"].str.contains(product_id.lower())]
    return row["lidvid"].item()


def main():
    parser = arg_parser()
    args = parser.parse_args()

    if args.output is None:
        args.output = args.yaml.with_suffix(".xml")

    # First read in the YAML to gather some introductory data.
    d = yaml.safe_load(args.yaml.read_text())
    d["vid"] = vid_max(d["modification_details"])

    if args.csv:
        # This is the trigger to assume that this is a label for a VIPER LROC Orthoimage,
        # which requires a little different handling.
        match = re.search(r"M\d+[RL]E", args.input.name, flags=re.I)
        if match:
            pid = match.group(0)
        else:
            parser.error(
                f"A PDS3 LROC Product ID could not be extracted from {args.input.name}"
            )

        # lroc_lidvid = get_lv(args.csv, args.input.name.split(".")[0])
        lroc_lidvid = get_lv(args.csv, pid)
        lroc_name = lroc_lidvid.split("::")[0].split(":")[-1]
        lid = lroc_name + "-ortho"
        args.output = Path(f"{lid}.xml")

        d["lid"] += lid
        d["title"] += " " + lroc_name

        d["source_product_internal"].append(
            {
                "lidvid": lroc_lidvid,
                "type": "data_to_derived_source_product",
                "comment": "The LROC NAC image which is orthorectified.",
            }
        )

    else:
        # check lid / filename consistency
        if d["lid"].split(":")[-1] != args.output.stem:
            parser.error(
                f"The LID ({d['lid']}) does not match the output filename ({args.output.stem})."
            )

    # Now gdal_translate
    opts = gdal.TranslateOptions(
        format="PDS4",
        creationOptions="IMAGE_FORMAT=GEOTIFF",
        outputSRS=args.projection,
    )
    gdal.Translate(str(args.output), str(args.input), options=opts)

    print(args.output)

    # Sort GeoTIFF file
    lbl_tif = args.output.with_suffix(".tif")

    # Now add some metadata to the TIFF itself.
    ds = gdal.OpenEx(str(lbl_tif), gdal.OF_RASTER | gdal.OF_UPDATE)
    md = ds.GetMetadata()
    md["TIFFTAG_DATETIME"] = date.today().isoformat()
    md["TIFFTAG_IMAGEDESCRIPTION"] = f"{d['title']}, {d['lid']}::{d['vid']}"
    ds.SetMetadata(md)

    # Read in GDAL XML and trim the broken element.
    root = ET.fromstring(args.output.read_text().replace("<cart: />", ""))

    # Add some empty entries so I don't have to remember to include them in every .yml file

    d.setdefault("obs_system_desc", False)

    if "obs_system_components" in d:
        for i, c in enumerate(d["obs_system_components"]):
            if "desc" not in c:
                d["obs_system_components"][i]["desc"] = False
            if "lid_ref" not in c:
                d["obs_system_components"][i]["lid_ref"] = False

    if "software_programs" in d:
        for i, p in enumerate(d["software_programs"]):
            if "desc" not in p:
                d["software_programs"][i]["desc"] = False
            if "params" not in p:
                d["software_programs"][i]["params"] = []

    d.setdefault("external_reference", [])
    d.setdefault("source_product_external", [])
    d.setdefault("source_product_internal", [])
    d.setdefault("proc_sw", False)
    d.setdefault("file_area_obs_supplemental", False)

    # d["moddate"] = date.today().isoformat()
    d["file_name"] = lbl_tif

    # Get things from the GDAL label
    d["west_bounding"] = find_text(root, ".//cart:west_bounding_coordinate")
    d["east_bounding"] = find_text(root, ".//cart:east_bounding_coordinate")
    d["north_bounding"] = find_text(root, ".//cart:north_bounding_coordinate")
    d["south_bounding"] = find_text(root, ".//cart:south_bounding_coordinate")
    d["pix_res"] = find_text(root, ".//cart:pixel_resolution_x")
    d["pix_scale"] = find_text(root, ".//cart:pixel_scale_x")
    d["ulx"] = find_text(root, ".//cart:upperleft_corner_x")
    d["uly"] = find_text(root, ".//cart:upperleft_corner_y")
    d["obj_length"] = find_text(
        root, ".//pds:File_Area_Observational/pds:Header/pds:object_length"
    )
    d["image_offset"] = find_text(
        root, ".//pds:File_Area_Observational/pds:Array_3D_Image/pds:offset"
    )
    d["axis_index_order"] = find_text(
        root, ".//pds:File_Area_Observational/pds:Array_3D_Image/pds:axis_index_order"
    )
    d["data_type"] = find_text(
        root,
        ".//pds:File_Area_Observational/pds:Array_3D_Image/pds:Element_Array/pds:data_type",
    )

    try:
        d["missing_constant"] = find_text(
            root,
            ".//pds:File_Area_Observational/pds:Array_3D_Image/pds:Special_Constants/pds:missing_constant",
        )
    except ValueError:
        d["missing_constant"] = False

    for axis in root.findall(".//pds:Array_3D_Image/pds:Axis_Array", ns):
        if find_text(axis, "pds:axis_name") == "Line":
            d["lines"] = find_text(axis, "pds:elements")

        if find_text(axis, "pds:axis_name") == "Sample":
            d["samples"] = find_text(axis, "pds:elements")

    if d["file_area_obs_supplemental"]:
        faos_path = Path(d["faos_file_name"])
        d["faos_creation_datetime"] = isozformat(
            datetime.fromtimestamp(faos_path.stat().st_mtime, timezone.utc)
        )

        with open(faos_path, "rb") as f:
            d["faos_records"] = sum(1 for _ in f)

    # print(d)

    # This overwrites the output file created by the run of gdal.Translate()
    write_xml(d, args.output, args.template)


if __name__ == "__main__":
    sys.exit(main())
