def solution(n):
    if n % 2 == 1:
        return 0
    elif n == 2:
        return 3
    elif n == 4:
        return 11
    else:
        a, b = 3, 11
        for _ in range(n//2 - 2):
            a, b = b, (b * 4 - a) % 1000000007
        return b