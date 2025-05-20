#! /usr/bin/env python3

"""weekday.py
=================

Print the weekday for the 13th day of every month across a 400 year span.

The script is intentionally simple: it only outputs the date strings and does
no additional processing.  It was originally inspired by a 2022 article in the
Dutch newspaper NRC Handelsblad.
"""

from datetime import date

# some settings

DAY_OF_MONTH = 13
START_YEAR = 1822

## main code

for year in range(0, 400):
    for month in range(1, 13):
        print(date(START_YEAR + year, month, DAY_OF_MONTH).ctime())
