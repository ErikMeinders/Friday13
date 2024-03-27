#! /usr/bin/env python3
"""
Test for find_repeat module
"""

from find_repeat import find_repeat

# some tests with expected outcome

print('Expected : 0 0 0 2 2 5 1 0')

a = find_repeat([1,2,1,2,2,3],True) 
b = find_repeat([1,2,1,2,1,3],True) 
c = find_repeat([1,2,1,2,1,2,3],True) 
d = find_repeat([1,2,1,2,1,2,1],True) 
e = find_repeat([1,2,1,2,1,2],True) 
f = find_repeat([1,2,1,2,3,1,2,1,2,3,1,2],True)
g = find_repeat([1,1,1,1], True)
h = find_repeat([range(10)], True)

print(f'Result is: {a} {b} {c} {d} {e} {f} {g} {h}')
