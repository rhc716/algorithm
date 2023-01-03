import math

def countDivisors(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt

def solution(number, limit, power):
    total = 0
    for n in range(1, number+1):
        cd = countDivisors(n)
        total += power if cd > limit else cd
    return total