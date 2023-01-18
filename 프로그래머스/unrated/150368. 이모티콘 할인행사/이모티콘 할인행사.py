from itertools import product

def solution(users, emoticons):
    for i, v in enumerate(emoticons):
        emoticons[i] = [[v, 40], [v, 30], [v, 20], [v, 10]]
    results = []
    for emo in product(*emoticons):
        t_member = 0
        t_price = 0
        for u in users:
            price = sum([e[0] * (100 - e[1]) * 0.01 for e in emo if u[0] <= e[1]])
            if price >= u[1]:
                t_member += 1
            else:
                t_price += price
        results.append([t_member, t_price])
    return sorted(results, reverse=True)[0]