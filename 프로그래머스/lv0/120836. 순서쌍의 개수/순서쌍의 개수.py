def solution(n):
    divisor_cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            divisor_cnt += 1
    return divisor_cnt