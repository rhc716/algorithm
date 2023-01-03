import math

def solution(denum1, num1, denum2, num2):
    a = denum1 * num2 + denum2 * num1
    b = num1 * num2
    c = math.gcd(a, b)
    return [a/c,b/c]