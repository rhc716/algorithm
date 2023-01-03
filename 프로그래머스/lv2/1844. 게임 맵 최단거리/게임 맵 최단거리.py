from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    queue = deque()
    queue.append([0,0])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            if 0 <= newx < n and 0 <= newy < m and maps[newx][newy] == 1:
                maps[newx][newy] = maps[x][y] + 1
                queue.append([newx,newy])
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1