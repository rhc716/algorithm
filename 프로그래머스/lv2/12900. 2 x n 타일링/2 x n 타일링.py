def solution(n):
    n2 = 0
    n1 = 1
    for i in range(1, n):
        t = n1
        n1 = n2 + n1
        n2 = t
    return (n2+n1) % 1000000007