from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for x in permutations(dungeons):
        t = k
        cnt = 0
        for y in x:
            if t >= y[0]:
                t -= y[1]
                cnt += 1
            else:
                break
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt