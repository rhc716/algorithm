def solution(s):
    zeroCnt = 0
    i = 0
    while s != '1':
        i += 1
        c = s.count('1')
        zeroCnt += len(s) - c
        s = str(bin(c))[2:]
    return [i, zeroCnt]