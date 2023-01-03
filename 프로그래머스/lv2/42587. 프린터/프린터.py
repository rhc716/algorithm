def solution(prio, loc):
    countP = 0
    while len(prio) > 0:
        first = prio.pop(0)
        if len(prio) > 0 and max(prio) > first:
            prio.append(first)
            if loc == 0:
                loc = len(prio) - 1
            else:
                loc -= 1
        else:
            countP += 1
            if loc == 0:
                break
            else:
                loc -= 1
    return countP