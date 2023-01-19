from itertools import combinations

def solution(line):
    stars = []
    for [A, B, E], [C, D, F] in combinations(line, 2):
        if A*D != B*C:
            p1 = (B*F - E*D)/(A*D - B*C) 
            p2 = (E*C - A*F)/(A*D - B*C)
            if p1 // 1 == p1 and p2 // 1 == p2:
                stars.append([int(p1), int(p2)])
    tmp = list(zip(*stars))
    result = []
    for y in range(max(tmp[1]), min(tmp[1]) - 1, -1):
        buf = ''
        for x in range(min(tmp[0]), max(tmp[0]) + 1):
            buf += '*' if [x, y] in stars else '.'
        result.append(buf)
    return result