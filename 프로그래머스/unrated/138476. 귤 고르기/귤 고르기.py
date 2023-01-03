from collections import Counter

def solution(k, tangerine):
    result = 0
    for key, val in sorted(Counter(tangerine).items(), key=lambda x:-x[1]):
        result += 1
        k -= val
        if k <= 0:
            break
    return result