def solution(s, num1, num2):    
    t = s[:num1] + s[num2] + s[num1 + 1:]
    return t[:num2] + s[num1] + t[num2 + 1:]