def solution(s):
    T = {}
    res = []
    for i, v in enumerate(s):
        if v in T:
           res.append(i - T[v])
        else:
            res.append(-1)
        T[v] = i
    return res