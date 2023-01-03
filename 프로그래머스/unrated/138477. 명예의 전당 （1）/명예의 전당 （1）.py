def solution(k, score):
    result = []
    tmp = []
    for s in score:
        tmp = sorted(tmp + [s])
        if len(tmp) > k:
            tmp.pop(0)
        result.append(tmp[0])
    return result