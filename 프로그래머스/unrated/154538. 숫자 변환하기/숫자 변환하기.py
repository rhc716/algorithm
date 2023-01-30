from collections import deque

def solution(x, y, n):
    visit = [-1] * (y + 1)
    q = deque([x])
    visit[x] = 0
    while q:
        v = q.popleft()
        if v + n <= y and visit[v + n] == -1:
            visit[v + n] = visit[v] + 1
            q.append(v + n)
        if v * 2 <= y and visit[v * 2] == -1:
            visit[v * 2] = visit[v] + 1
            q.append(v * 2)
        if v * 3 <= y and visit[v * 3] == -1:
            visit[v * 3] = visit[v] + 1
            q.append(v * 3)
    return visit[y]

# 완전 탐색 (bfs) : 가장 최단으로 도달한 것을 구하는 것이므로
# 3 가지 경우로 계속 쪼개져 나감 : +n, *2, *3 : y 초과 체크
# visit 여부 체크 : 도달하는데 걸린 횟수 : 초기값 -1