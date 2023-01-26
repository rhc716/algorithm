from itertools import product

def solution(n, info):
    res = [-1]
    max_gap = 0
    for win_ryan in product([True, False], repeat=11): 
        info_ryan = [info[i] + 1 if win_ryan[i] else 0 for i in range(11)]
        if sum(info_ryan) <= n:
            score_ryan = sum([10 - i for i in range(11) if win_ryan[i]])
            score_apeach = sum([10 - i for i in range(11) if not win_ryan[i] and info[i]])
            gap = score_ryan - score_apeach
            if gap > 0 and gap >= max_gap:
                info_ryan[-1] += n - sum(info_ryan)
                if gap == max_gap:
                    for i, j in zip(info_ryan[::-1], res[::-1]):
                        if i < j:
                            break
                        elif i > j:
                            res = info_ryan
                            break
                else:
                    max_gap = gap
                    res = info_ryan
    return res