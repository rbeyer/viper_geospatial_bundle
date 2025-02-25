#!/usr/bin/env python
"""Converts the sfs_images.csv to sfs_orthos.csv.
"""

import argparse
import csv
from pathlib import Path
import sys


def arg_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument("input", type=Path, help="Input sfs_images CSV file.")
    parser.add_argument("output", type=Path, help="Output sfs_orthos CSV file.")

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    with open(args.input, newline="") as csvin, open(
        args.output, "w", newline=""
    ) as csvout:
        reader = csv.reader(csvin)
        writer = csv.writer(csvout, lineterminator="\n")
        for row in reader:
            naclid = row[1].split("::")[0].split(":")[-1]
            ortholid = (
                f"urn:nasa:pds:viper_geospatial:lroc_orthoimages:{naclid}-ortho::1.0"
            )
            writer.writerow([row[0], ortholid])


if __name__ == "__main__":
    sys.exit(main())
