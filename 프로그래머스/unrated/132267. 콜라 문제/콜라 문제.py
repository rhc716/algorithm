def solution(a, b, n):
    sum_cola = 0
    while n // a > 0:
        sum_cola += (n // a) * b
        n = (n // a) * b + n % a
    return sum_cola