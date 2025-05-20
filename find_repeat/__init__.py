"""Utility functions for detecting repeating patterns in sequences."""

from typing import Sequence, Any


def find_repeat(items: Sequence[Any], verbose: bool = False) -> int:
    """Return the length of the shortest repeating pattern in *items*.

    If no repeating pattern is found, ``0`` is returned.
    """

    def _debug(msg: str) -> None:
        if verbose:
            print(msg)

    _debug(f"\nfinding repeating pattern in list: {items}")

    n = len(items)
    for pat_len in range(1, n // 2 + 1):
        pattern = items[:pat_len]
        _debug(f"Try pattern: {pattern}")

        max_pats, remaining = divmod(n, pat_len)
        _debug(
            f"With a length of {pat_len} a maximum of {max_pats} full patterns would fit, with {remaining} items remaining"
        )

        match = True
        for rpt in range(1, max_pats):
            candidate = items[pat_len * rpt : pat_len * (rpt + 1)]
            _debug(f"pat_{rpt}: {candidate}")
            if candidate != pattern:
                _debug(f"pattern fails in {rpt}th repetition")
                match = False
                break

        if match and remaining:
            _debug("Pattern repeats {max_pats} times, now inspect remainder")
            _debug(f"Remaining {remaining} items check")
            if items[:remaining] != items[max_pats * pat_len :]:
                _debug("candidate fails in tail")
                match = False

        if match:
            _debug(f"Full pattern match with length {pat_len}!")
            return pat_len

    _debug("No pattern match!")
    return 0
