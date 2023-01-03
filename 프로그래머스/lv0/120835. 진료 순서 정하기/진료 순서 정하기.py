def solution(emergency):
    t = sorted(emergency)[::-1]
    return [t.index(e) + 1 for e in emergency]