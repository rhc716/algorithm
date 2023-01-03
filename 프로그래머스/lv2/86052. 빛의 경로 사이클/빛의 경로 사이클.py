from collections import deque

def solution(grid):
    fourDir = ((-1,0),(0,-1),(1,0),(0,1))
    cycles = set()
    length = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                leng = 0
                while (i,j,d) not in cycles:
                    cycles.add((i,j,d))
                    if grid[i][j] == 'L':
                        d = (d + 1) % 4
                    elif grid[i][j] == 'R':
                        d = (d - 1) % 4
                    i = (i + fourDir[d][0]) % len(grid)
                    j = (j + fourDir[d][1]) % len(grid[0])
                    leng += 1
                if leng > 0:
                    length.append(leng)
    return sorted(length)
