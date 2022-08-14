#! /usr/bin/env python3.9
"""
Test for find_repeat module
"""

from find_repeat import find_repeat

# some tests with expected outcome

print('Expected : 0 0 0 2 2 5')

a = find_repeat([1,2,1,2,2,3]) 
b = find_repeat([1,2,1,2,1,3]) 
c = find_repeat([1,2,1,2,1,2,3]) 
d = find_repeat([1,2,1,2,1,2,1]) 
e = find_repeat([1,2,1,2,1,2]) 
f = find_repeat([1,2,1,2,3,1,2,1,2,3,1,2])

print(f'Result is: {a} {b} {c} {d} {e} {f}')
