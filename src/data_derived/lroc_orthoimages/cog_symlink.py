#!/usr/bin/env python
"""
Creates symbolic links from the VIPER source CoGs to this directory, with
appropriate filenames for ease of Makefile processing.
"""

import argparse
import csv
from pathlib import Path
import sys


def arg_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument("input", type=Path, nargs="+", help="Path to VIPER source CoG.")

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    for p in args.input:
        # Assumes that p is <product_id>_map.tif
        pid = p.stem.split(".")[0]
        cogsym_path = Path(f"COG-nac.{pid.lower()}.tif")

        cogsym_path.symlink_to(p)


if __name__ == "__main__":
    sys.exit(main())
