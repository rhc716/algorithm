from itertools import combinations

def solution(dots):
    lines = list(combinations(dots, 2))
    for i in range(3):
        p1 = lines[i][0]
        p2 = lines[i][1]
        p3 = lines[-(i+1)][0]
        p4 = lines[-(i+1)][1]
        if p2[0]-p1[0] == 0 and p4[0]-p3[0] == 0:
            return 1
        elif p2[0]-p1[0] == 0 or p4[0]-p3[0] == 0:
            continue
        else:
            gradi1 = (p2[1]-p1[1])/(p2[0]-p1[0])
            gradi2 = (p4[1]-p3[1])/(p4[0]-p3[0])
            if gradi1 == gradi2:
                return 1
    return 0