from itertools import product

def solution(places):
    res = []
    for p in places:
        p = ["OOOOOOO"] + [ 'O'+s+'O' for s in p] + ["OOOOOOO"]
        for i, j in product(range(1, 6), range(1, 6)):
            if (p[i][j] == 'P' and 'P' in [p[i-1][j], p[i][j-1], p[i+1][j], p[i][j+1]]) or \
               (p[i][j] == 'O' and [p[i-1][j], p[i][j-1], p[i+1][j], p[i][j+1]].count('P') > 1):
                res.append(0)
                break
        else:
            res.append(1)
    return res