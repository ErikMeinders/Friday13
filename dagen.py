#! /usr/bin/env python

from datetime import date
import calendar

# some settings

dag_van_de_maand = 13
startjaar=1400

## main code

dagen = [] # maakt een leeg array genaamd dagen


# range(van, tot) --> let op, niet (van, totenmet)!!
# vul het dagen array met de weekdag voor de 13e van iedere maand voor een periode van 800 jaar

for jaar in range(0, 400):
  for maand in range (1, 13):
    print(date(startjaar + jaar , maand, dag_van_de_maand).ctime())

