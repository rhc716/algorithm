def solution(n):
    f0 = 0
    f1 = 1
    for _ in range(1, n):
        f0, f1 = f1, f1 + f0
    return f1 % 1234567