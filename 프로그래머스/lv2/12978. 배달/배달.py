from math import inf

def solution(N, road, K):
    floyd = [[inf]*N for _ in range(N)]
    for i in range(N):
        floyd[i][i] = 0
    for s, d, t in road:
        if floyd[s-1][d-1] > t:
            floyd[s-1][d-1] = t
        if floyd[d-1][s-1] > t:
            floyd[d-1][s-1] = t
    for t in range(N):
        for i in range(N):
            for j in range(N):
                if floyd[i][j] > floyd[i][t] + floyd[t][j]:
                    floyd[i][j] = floyd[i][t] + floyd[t][j]
    return sum(n <= K for n in floyd[0])