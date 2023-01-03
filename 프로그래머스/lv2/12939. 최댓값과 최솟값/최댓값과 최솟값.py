def solution(s):
    t = list(map(int, s.split(' ')))
    return f"{min(t)} {max(t)}"