def solution(n):
    f = 1
    i = 1
    while f * i <= n:
        f *= i
        i += 1
    return i - 1