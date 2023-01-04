def solution(num, k):
    f = str(num).find(str(k))
    return f+1 if f > -1 else -1