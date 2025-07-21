#!/usr/bin/env python3
"""tally.py
==========
Count occurrences of weekday names from stdin.

Use together with `weekday.py` like:
    ./weekday.py | ./tally.py
"""

from collections import Counter
import sys

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def tally_stream(stream):
    """Return a Counter with occurrences of first words in each line."""
    counts = Counter()
    for line in stream:
        if not line.strip():
            continue
        word = line.split()[0]
        counts[word] += 1
    return counts


def main():
    counts = tally_stream(sys.stdin)
    for day in WEEKDAYS:
        print(f"{day} : {counts.get(day, 0)}")


if __name__ == "__main__":
    main()
