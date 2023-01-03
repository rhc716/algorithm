from itertools import cycle

def solution(answers):
    scores = []
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]] 
    for i in range(3):
        scores.append(sum([1 if p == a else 0 for p, a in zip(cycle(patterns[i]), answers)]))
    sm = max(scores)
    return list(map(lambda x:x+1, [i for i, x in enumerate(scores) if x == sm]))