# Friday 13
How often is the 13th of a month on a Friday? And is that more often than any other day of the week?

# The question

In my (Dutch) newspaper on some Friday 13th, I read an article on the likelyhood of a 13th of a month to be Friday.
It stated Friday was actually the most likely day for any 13th of the month - which puzzled me.
I would think that in the grand scheme of things, all days are equal ...
It triggered me to write a quick python program to verify this statement.

## Usage

The scripts in this repository contain a shebang so they can be executed
directly from the command line.  Set the executable bit once with

```bash
chmod +x weekday.py tally.py leapeat.py
```

After that you can invoke the tools like normal commands.

# weekday

`weekday.py` prints the weekday of the 13th day of every month.  By default it
shows a span of 400 years (400×12 = 4800 months), but you can override both the
start year and the amount of years to inspect with command line flags.

```bash
./weekday.py --start 2025 --years 75
```

The example above lists the weekdays for the 13th day of every month for the
next 75 years.

The reason to take 400 years in consideration is related to the leap-year rules.
The periodicity is 400 years (since 1752):

February has 29 days:

- when the year is a multiple of 4 (1924 is a leap year)
- except when the year is a multiple of 100 (1700, 1800 and 1900 were not leap years)
- except except when the year is a multiple of 400 (2000 is a leap year)
- the identical 1800 and 2200 calendars

# tally

`tally.py` reads the output of `weekday.py` and counts how often each weekday occurs.
Use it as: `./weekday.py [--start YEAR] [--years NUM] | ./tally.py`

Counting the weekdays of the 13th day of the 4800 months gives:

Mon :      685
Tue :      685
Wed :      687
Thu :      684
Fri :      688
Sat :      684
Sun :      687

This is regardless the start-year always the same.

So, in the long run and by a small margin, the 13th day of any month is most likely to be a Friday!

Happy Fridays.

# is 400 years really the minimum?

Then I wondered if the pattern of weekdays would repeat any sooner than after 4800 months, 
thats what leapeat.py aims to find out.

It uses a module in this repo named `find_repeat`.

`find_repeat` finds the shortest continuously repeating pattern in a list.
Unit tests for this module live in the `tests` directory and can be run with
`python -m unittest discover -s tests`.

# Inspiration

For those of you with an NRC subscription: https://www.nrc.nl/nieuws/2022/05/13/vrijdag-de-13de-a4124263
