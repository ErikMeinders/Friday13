#! /usr/bin/env python3.9

"""
quick hack to find distribution of the 13th day of the month over the weekdys
inspired by article in NRC Handelsblad in 2022
"""

from datetime import date

# some settings

MAANDDAG = 13
STARTJAAR=1622

## main code

dagen = [] # maakt een leeg array genaamd dagen

# range(van, tot) --> let op, niet (van, totenmet)!!
# vul het dagen array met de weekdag voor de 13e van iedere maand voor een periode van 800 jaar

for jaar in range(0, 400):
    for maand in range (1, 13):
        print(date(STARTJAAR + jaar , maand, MAANDDAG).ctime())
