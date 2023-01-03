from math import ceil

def solution(citations):
    h = 0
    half = ceil(len(citations)/2)
    for i in range(half, max(citations)+1):
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
            if cnt >= i and h < i:
                h = i
                break
    return h