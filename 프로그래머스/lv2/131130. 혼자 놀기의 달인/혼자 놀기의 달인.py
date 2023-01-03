def solution(cards):
    cards = {i + 1 : v for i, v in enumerate(cards)}
    groups = []
    tmp = []
    i = 1
    while len(cards) > 0:
        if i in cards:
            tmp.append(i)
            tmp2 = cards[i]
            del cards[i]
            i = tmp2
            if len(cards) == 0:
                groups.append(tmp)
        else:
            groups.append(tmp)
            tmp = []
            i = list(cards.keys())[0]
    lens = sorted([len(x) for x in groups])
    return 0 if len(lens) == 1 else lens[-2] * lens[-1]