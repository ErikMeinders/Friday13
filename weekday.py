#! /usr/bin/env python3

"""weekday.py
=================

Print the weekday for the 13th day of every month across a 400 year span.

The script is intentionally simple: it only outputs the date strings and does
no additional processing.  It was originally inspired by a 2022 article in the
Dutch newspaper NRC Handelsblad.
"""

from datetime import date
import argparse

DAY_OF_MONTH = 13
DEFAULT_START_YEAR = 1822
DEFAULT_YEARS = 400


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Print the weekday for the 13th day of each month")
    parser.add_argument(
        "--start",
        type=int,
        default=DEFAULT_START_YEAR,
        help="first year to report (default: %(default)s)",
    )
    parser.add_argument(
        "--years",
        type=int,
        default=DEFAULT_YEARS,
        help="how many years to show (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for year in range(args.start, args.start + args.years):
        for month in range(1, 13):
            print(date(year, month, DAY_OF_MONTH).ctime())


if __name__ == "__main__":
    main()
