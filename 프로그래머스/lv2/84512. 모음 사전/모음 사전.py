from itertools import product

def solution(word):
    _dict = []
    for i in range(1,6):
        _dict.extend([''.join(x) for x in product('AEIOU', repeat=i)])
    return sorted(_dict).index(word)+1