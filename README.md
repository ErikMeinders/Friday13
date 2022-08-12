# Friday13
How often is the 13th of a month on a Friday and is that more often than any other day.

# The question

In my (Dutch) newspaper on some Friday 13th I read an article on the likelyhood of a 13th of a month to be Friday.
It stated Friday was actually the most likely day for any 13th of the month - which puzzled me.
It triggered me to write a quick python program to verify this statement.

# dagen

dagen.py (dagen is Dutch for days)

dagen.py outputs the weekday of the 13th day of any month in a 400 year period (400*12 = 4800 days).

The program starts in a configurable year and does the math.

The reason to take 400 years in consideration is related to the leap-year rules.
The periodicity is 400 years:

February has 29 days:

- when the year divides by 4 (1924 is a leap year)
- except when the year is a multiple of 100 (1700, 1800 and 1900 were not leap years)
- except except when the year is a multiple of 400 (2000 is a leap year)

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

Then I wondered if the pattern of weekdays would repeat any sooner than after 4800 months, 
thats what pattern.py aims to find out.

There's plenty of comment in the file, in Dutch ....
