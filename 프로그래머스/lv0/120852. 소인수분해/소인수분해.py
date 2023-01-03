import math

def solution(n):
    ans = set()
    sqrt = int(math.sqrt(n))
    i = 2
    while i <= sqrt:
        if n % i == 0:
            ans.add(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        ans.add(n)
    return sorted(list(ans))