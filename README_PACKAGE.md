# find_repeat

A utility function for detecting repeating patterns in sequences.

## Installation

You can install the package via pip:

```bash
pip install find_repeat
```

## Usage

```python
from find_repeat import find_repeat

# Find the repeating pattern in a sequence
pattern_length = find_repeat([1, 2, 1, 2, 1, 2])
print(f"The pattern repeats every {pattern_length} items")  # Output: The pattern repeats every 2 items

# If no pattern is found, 0 is returned
no_pattern = find_repeat([1, 2, 3, 4, 5])
print(f"Pattern length: {no_pattern}")  # Output: Pattern length: 0

# You can enable verbose output to see the detection process
find_repeat([1, 2, 1, 2, 1, 2], verbose=True)
```

## Function Documentation

### find_repeat(items, verbose=False)

Return the length of the shortest repeating pattern in *items*.

If no repeating pattern is found, `0` is returned.

#### Parameters:
- `items` (Sequence[Any]): The sequence to check for patterns
- `verbose` (bool): Whether to print debug information during pattern detection

#### Returns:
- `int`: The length of the shortest repeating pattern, or 0 if no pattern is found