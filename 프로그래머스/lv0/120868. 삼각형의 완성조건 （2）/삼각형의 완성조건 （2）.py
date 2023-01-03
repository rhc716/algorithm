def solution(sides):
    n = min(sides)
    x = max(sides)
    p = [x for x in range(x-n+1,x+1)] + [x for x in range(x+1, n+x)]
    return len(p)