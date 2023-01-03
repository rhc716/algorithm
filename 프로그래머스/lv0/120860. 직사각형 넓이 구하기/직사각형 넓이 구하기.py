def solution(dots):
    l = [x for x, y in dots]
    r = [y for x, y in dots]
    print(min(dots))
    return (max(l) - min(l)) * (max(r) - min(r))