def solution(n):
    base3 = ''
    while n:
        base3 += str(n % 3)
        n //= 3
    return int(base3, 3)