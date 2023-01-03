def solution(n):
    res = 0
    for i in range(1, n + 1):
        s = 0
        for j in range(n):
            s += i+j
            if s == n:
                res += 1
            if s >= n:
                break
    return res