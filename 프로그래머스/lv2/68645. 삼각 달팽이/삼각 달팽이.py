def solution(n):
    list2D = [[0]*(i+1) for i in range(n)]
    x, y = -1, 0
    v = 1
    for i in range(n): 
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            list2D[x][y] = v
            v += 1
    return sum(list2D, [])