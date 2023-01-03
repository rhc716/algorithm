def solution(k, m, score):
    score.sort(reverse=True)
    res = 0
    for x in [score[i:i+m] for i in range(0, len(score), m)]:
        if len(x) == m:
            res += min(x) * m
    return res