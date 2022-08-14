#! /usr/bin/env python3.9

"""
quick hack to find distribution of the 13th day of the month over the weekdys
inspired by article in NRC Handelsblad in 2022
"""

from datetime import date

# some settings

DAY_OF_MONTH = 13
STARTYEAR=1822

## main code

days = [] # maakt een leeg array genaamd days

for year in range(0, 400):
    for month in range (1, 13):
        print(date(STARTYEAR + year , month, DAY_OF_MONTH).ctime())
