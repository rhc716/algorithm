def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget <= 0:
            return i if budget < 0 else i + 1
    return len(d)