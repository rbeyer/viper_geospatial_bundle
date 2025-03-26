#!/usr/bin/env python
"""Really just a minor bump to basic labelmaker capability.
"""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

import yaml

from vipersci.pds.datetime import isozformat
from vipersci.pds.labelmaker import vid_max, write_xml


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
        "-t", "--template", type=Path, help="XML template to use to create the output."
    )
    parser.add_argument("-y", "--yaml", type=Path, help="The YAML file to load.")

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    # Now read in the YAML to populate the dictionary.
    d = yaml.safe_load(args.yaml.read_text())

    d["file_name"] = args.csv
    d["vid"] = vid_max(d["modification_details"])

    file_path = Path(d["file_name"])
    d["file_creation_datetime"] = isozformat(
        datetime.fromtimestamp(file_path.stat().st_mtime, timezone.utc)
    )

    with open(file_path, "rb") as f:
        d["records"] = sum(1 for _ in f)

    # print(d)

    write_xml(d, args.output, args.template)


if __name__ == "__main__":
    sys.exit(main())
