def solution(n):
    c = bin(n).count('1')
    i = 0
    while True:
        i += 1
        if bin(n + i).count('1') == c:
            return n + i
    return 0