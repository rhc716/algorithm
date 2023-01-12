from collections import deque

def bfs(start, childs, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in childs[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, wires):
    gaps = []
    for i, [start, end] in enumerate(wires):
        visited = [False] * (n + 1)
        childs = [[] for _ in range(n + 1)]
        for j, [a, b] in enumerate(wires):
            if i == j:
                continue
            childs[a].append(b)
            childs[b].append(a)
        bfs(start, childs, visited)
        gaps.append(abs(n - sum(visited[1:])*2))
    return min(gaps)