#!/usr/bin/env python
"""Starts by reading information from a PDS4 label from GDAL, gathers
other information, and then writes a more specfic label.
"""

import argparse
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET
import sys

import pandas as pd

from vipersci.pds.labelmaker import write_xml
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
    parser.add_argument("input", type=Path, help="Input XML label written by GDAL.")

    return parser


def get_lv(path, product_id):

    df = pd.read_csv(path, names=["reference_type", "lidvid"])

    row = df[df["lidvid"].str.contains(product_id.lower())]

    return row["lidvid"].get(0)


def main():
    parser = arg_parser()
    args = parser.parse_args()

    lroc_lidvid = get_lv(args.csv, args.input.name.split(".")[0])
    lroc_name = lroc_lidvid.split("::")[0].split(":")[-1]

    # Read in GDAL XML and trim the broken element.
    root = ET.fromstring(args.input.read_text().replace("<cart: />", ""))

    # Sort output files.
    if args.output is None:
        args.output = Path(f"{lroc_name}-ortho.xml")

    gdal_tif = args.input.with_suffix(".tif")
    lbl_tif = args.output.with_suffix(".tif")
    if gdal_tif.exists():
        gdal_tif.rename(lbl_tif)

    # Now build dictionary for the template.
    d = {}

    d["lid"] = f"urn:nasa:pds:viper_geospatial:lroc_orthoimages:{lroc_name}-ortho"
    d["lrocnac_name"] = lroc_name
    d["moddate"] = date.today().isoformat()
    d["west_bounding"] = find_text(root, ".//cart:west_bounding_coordinate")
    d["east_bounding"] = find_text(root, ".//cart:east_bounding_coordinate")
    d["north_bounding"] = find_text(root, ".//cart:north_bounding_coordinate")
    d["south_bounding"] = find_text(root, ".//cart:south_bounding_coordinate")
    d["pix_res"] = find_text(root, ".//cart:pixel_resolution_x")
    d["pix_scale"] = find_text(root, ".//cart:pixel_scale_x")
    d["ulx"] = find_text(root, ".//cart:upperleft_corner_x")
    d["uly"] = find_text(root, ".//cart:upperleft_corner_y")
    d["lroclidvid"] = lroc_lidvid
    d["file_name"] = lbl_tif
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

    # print(d)

    write_xml(d, args.output, args.template)

    args.input.unlink()


if __name__ == "__main__":
    sys.exit(main())
