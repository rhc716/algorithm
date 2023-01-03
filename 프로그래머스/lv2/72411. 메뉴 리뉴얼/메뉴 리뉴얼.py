from itertools import combinations

def solution(orders, course):
    menu = {}
    ans = []
    for o in orders:
        for i in range(1, len(o)+1):
            for s in combinations(o, i):
                k = ''.join(sorted(s))
                if k in menu:
                    menu[k] += 1
                elif len(k) in course:
                    menu[k] = 1
    for c in course:
        d = {m : menu[m] for m in menu if menu[m] > 1 and len(m) == c}
        if d:
            mv = max(d, key=d.get)
            ans.extend([key for key,value in d.items() if d[mv] == value])
    return sorted(ans)