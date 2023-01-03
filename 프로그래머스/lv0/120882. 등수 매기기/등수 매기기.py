def solution(score):
    d = {}
    d2 = {}
    for i, s in enumerate(score):
        d[i+1] = sum(s)
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    beforeKey = -1
    beforeVal = -1
    for i, v in enumerate(sorted_d):
        if beforeVal == v[1]:
            d2[v[0]] = d2[beforeKey]
        else:
            d2[v[0]] = i + 1
        beforeKey = v[0]
        beforeVal = v[1]
    return [d2[k] for k in sorted(d2)]