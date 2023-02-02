from math import gcd
from functools import reduce

def factors(arr):
    if not arr:
        return set()
    g = reduce(gcd, arr)
    return set(f for f in range(1, g + 1) if g % f == 0)

def solution(arrayA, arrayB):
    arrayA, arrayB = set(arrayA) - set(arrayB), set(arrayB) - set(arrayA)
    af, bf = factors(arrayA), factors(arrayB)
    res = set([0])
    for a in af-bf:
        if all(b % a != 0 for b in arrayB):
            res.add(a)
    for b in bf-af:
        if all(a % b != 0 for a in arrayA):
            res.add(b)
    return max(res)