# Friday 13
How often is the 13th of a month on a Friday? And is that more often than any other day of the week?

# The question

In my (Dutch) newspaper on some Friday 13th I read an article on the likelyhood of a 13th of a month to be Friday.
It stated Friday was actually the most likely day for any 13th of the month - which puzzled me.
It triggered me to write a quick python program to verify this statement.

# dagen

dagen.py (dagen is Dutch for days)

dagen.py outputs the weekday of the 13th day of any month in a 400 year period (400*12 = 4800 days).

The program starts in a configurable year and does the math.

The reason to take 400 years in consideration is related to the leap-year rules.
The periodicity is 400 years (since 1752):

February has 29 days:

- when the year divides by 4 (1924 is a leap year)
- except when the year is a multiple of 100 (1700, 1800 and 1900 were not leap years)
- except except when the year is a multiple of 400 (2000 is a leap year)
- the identical 1800 and 2200 calendars

# turf

A quick script (turf is Dutch for tally) runs the python code 7 times (one for each day) and count the occurences of all day-names (I know, bad code).

Counting the weekdays of the 13th day of the 4800 months gives:

Mon :      685
Tue :      685
Wed :      687
Thu :      684
Fri :      688
Sat :      684
Sun :      687

This is regardless the start-year always the same.

So, by a small margin, the 13th day of any month is most likely to be a Friday!

Happy Fridays.

# is 400 years really the minimum?

Then I wondered if the pattern of weekdays would repeat any sooner than after 4800 months, 
thats what leapeat.py aims to find out.

It uses a module in this repo named find_repeat

find_repeat_test.py is a standalone test-script for the find_repeat module.

# Inspiration

For those of you with an NRC subscription: https://www.nrc.nl/nieuws/2022/05/13/vrijdag-de-13de-a4124263
