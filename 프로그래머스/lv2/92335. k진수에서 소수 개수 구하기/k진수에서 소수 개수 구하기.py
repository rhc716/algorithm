import numpy
import math

def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a == 0:
            return False
        a += 1
    return num > 1

def solution(n, k):
    return sum([1 for x in numpy.base_repr(n, k).split('0') if not (x == '' or x == '1') and isprime(int(x))])