from fractions import Fraction

def solution(a, b):
    boonmo = Fraction(a, b).denominator
    i = 2
    while i <= boonmo:
        if i % 2 and i % 5 and boonmo % i == 0:
            return 2
        i += 1
    return 1