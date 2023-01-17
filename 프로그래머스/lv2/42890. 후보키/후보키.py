from itertools import combinations

def solution(relation):
    answer = []
    columnIdxs = [i for i in range(len(relation[0]))]
    for i in range(1, len(relation[0]) + 1):
        for comb in combinations(columnIdxs, i):
            if any([(all([a in comb for a in ans])) for ans in answer]): # 최소성
                continue
            tmp = []
            for j in range(len(relation)):
                s = ''
                for k in comb:
                    s += relation[j][k]
                tmp.append(s)
            if len(tmp) == len(set(tmp)): # 유일성
                answer.append(comb)
    return len(answer)