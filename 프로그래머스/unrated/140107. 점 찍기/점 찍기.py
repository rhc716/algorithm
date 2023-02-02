def solution(k, d):
    res = 0
    for x in range(0, d+1, k):
        maxY = int((d**2 - x**2) ** 0.5)
        res += len(range(0, maxY+1, k))
    return res