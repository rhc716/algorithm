def solution(s):
    sp = s.split(' ')
    while 'Z' in sp:
        i = sp.index('Z')
        sp.pop(i)
        if i > 0:
            sp.pop(i - 1)
    return sum(list(map(int, sp)))