#! /usr/bin/env python3.9
"""
Does the day of the week for a fixed day of the month pattern repeat before 400 years?

We know after 400 years it repeats:

- year is multiple of 4: leapyear
- year in multiple of 100: no leapyear
- year is multiple of 400: leapyear

AND

the calendar 1800 is the same as calendar 2200

NOTE: use a startyear after 1752!

"""

from datetime import date
from find_repeat import find_repeat

DAY_OF_THE_MONTH = 13
STARTYEAR=1753
YEARS=1800

###

days = []

for year in range(0, YEARS):
    for month in range (1, 13):
        days.append ( date(STARTYEAR + year , month, DAY_OF_THE_MONTH).weekday() )

# find the shortest repeating pattern

repeat_after = find_repeat(days)
print(f"Starting in the year {STARTYEAR}, the pattern repeats after {repeat_after} months")
