import math
from collections import Counter

def solution(clothes):
    return math.prod([1 + x for x in Counter([a[1]for a in clothes]).values()]) - 1