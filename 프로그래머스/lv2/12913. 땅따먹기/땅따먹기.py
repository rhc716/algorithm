def solution(land):
    for i in range(len(land)-1):
        for j in range(4):
            tmp = land[i][j]
            land[i][j] = 0
            land[i+1][j] += max(land[i])
            land[i][j] = tmp
    return max(land[-1])