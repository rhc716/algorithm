from collections import Counter

def solution(topping):
    personA = Counter(topping)
    personB = set()
    cutCnt = 0
    while topping:
        x = topping.pop()
        personA[x] -= 1
        if personA[x] == 0:
            del personA[x]
        personB.add(x)
        if len(personA) == len(personB):
            cutCnt += 1
        else:
            if cutCnt > 0:
                break
    return cutCnt