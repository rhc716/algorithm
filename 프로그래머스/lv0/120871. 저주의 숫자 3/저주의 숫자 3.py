def solution(n):
    i, m = 0, 0
    while n > m:
        i += 1
        if i % 3 == 0 or '3' in str(i):
            continue
        else:
            m += 1
    return i