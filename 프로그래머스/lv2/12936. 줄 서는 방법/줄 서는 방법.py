from math import factorial

def solution(n, k):
    arr = list(range(1, n + 1))
    res = []
    for i in range(n, 0, -1):
        a, b = divmod(k, factorial(i) // i)
        if b > 0:
            res.append(arr.pop(a))
        else:
            res.append(arr.pop(a-1))
        k = b
    return res