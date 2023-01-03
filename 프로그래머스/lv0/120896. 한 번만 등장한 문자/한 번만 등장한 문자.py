from collections import Counter

def solution(s):
    ct = Counter(s)
    return ''.join(sorted([c for c in ct if ct[c] == 1]))