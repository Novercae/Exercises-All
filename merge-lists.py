"""
Merge lists without repeat number.

expected return = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
"""

a = [1,2,3,4]
b = [1,3,4,5,6,7]
c = [3,6,8,9,10]

from heapq import  merge

def meg(*iterator):
    value, before = merge(*iterator), merge(*iterator)
    yield next(value)
    yield from (x for x, p in zip(value, before) if p != x)

print(list(meg(a, b, c)))
