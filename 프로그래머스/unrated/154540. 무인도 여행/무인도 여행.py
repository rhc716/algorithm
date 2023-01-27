import sys

def solution(maps):
    sys.setrecursionlimit(3600)
    answer = []
    visit = set()
    def dfs(i, j):
        if 0 <= i < len(maps) and 0 <= j < len(maps[0]) and maps[i][j] != 'X' and (i, j) not in visit:
            visit.add((i, j))
            return int(maps[i][j]) + dfs(i, j-1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1, j)
        else:
            return 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            f = dfs(i, j)
            if f > 0:
                answer.append(f)
    return [-1] if not answer else sorted(answer)