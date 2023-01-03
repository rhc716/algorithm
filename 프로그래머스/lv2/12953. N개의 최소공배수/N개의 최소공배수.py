import math

def solution(arr):
    a = 1
    for b in arr:
        a = (a * b) // math.gcd(a, b)
    return a