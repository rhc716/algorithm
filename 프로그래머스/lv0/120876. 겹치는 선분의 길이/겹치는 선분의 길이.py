def solution(lines):
    lines = [set(range(min([x,y]), max([x,y])+1)) for x, y in lines]
    a = lines[0] & lines[1]
    b = lines[0] & lines[2]
    c = lines[1] & lines[2]
    valid = [x for x in [a,b,c] if len(x) > 1]
    union = sorted(list(set().union(*valid)))
    res = 0
    for i in range(len(union) - 1):
        if union[i+1] - union[i] == 1:
            res += 1
    return res