def solution(n):
    p = n**0.5
    return (p+1)**2 if p==int(p) else -1