#!/usr/bin/env python
"""Starts by reading information from a PDS4 label from GDAL, gathers
other information, and then writes a more specfic label.
"""

import argparse
from datetime import date, datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
import sys

import yaml

from vipersci.pds.datetime import isozformat
from vipersci.pds.labelmaker import vid_max, write_xml
from vipersci.pds.xml import find_text, ns


def arg_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument(
        "-t", "--template", type=Path, help="XML template to use to create the output."
    )
    parser.add_argument("-o", "--output", type=Path, help="Output XML label file.")
    parser.add_argument("-c", "--csv", help="The csv file of LROC LIDVIDS to read.")
    parser.add_argument("-y", "--yaml", type=Path, help="The YAML file to load.")
    parser.add_argument("input", type=Path, help="Input XML label written by GDAL.")

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    # Read in GDAL XML and trim the broken element.
    root = ET.fromstring(args.input.read_text().replace("<cart: />", ""))

    # Now read in the YAML to populate the dictionary.
    d = yaml.safe_load(args.yaml.read_text())

    # Add some empty entries so I don't have to remember to include them in every .yml file
    for i, p in enumerate(d["software_programs"]):
        if "desc" not in p:
            d["software_programs"][i]["desc"] = False
        if "params" not in p:
            d["software_programs"][i]["params"] = []

    d.setdefault("external_reference", [])
    d.setdefault("source_product_external", [])
    d.setdefault("source_product_internal", [])
    d.setdefault("file_area_obs_supplemental", False)

    # check lid / filename consistency
    if d["lid"].split(":")[-1] != args.output.stem:
        parser.error(
            f"The LID ({d['lid']}) does not match the output filename ({args.output.stem})."
        )

    # Sort GeoTIFF file
    gdal_tif = args.input.with_suffix(".tif")
    lbl_tif = args.output.with_suffix(".tif")
    if gdal_tif.exists():
        gdal_tif.rename(lbl_tif)

    d["moddate"] = date.today().isoformat()
    d["file_name"] = lbl_tif
    d["vid"] = vid_max(d["modification_details"])

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
    d["missing_constant"] = find_text(
        root,
        ".//pds:File_Area_Observational/pds:Array_3D_Image/pds:Special_Constants/pds:missing_constant",
    )

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

    write_xml(d, args.output, args.template)

    args.input.unlink()


if __name__ == "__main__":
    sys.exit(main())
