def solution(s):
    correct = 0
    check = ['[]', '()', '{}']
    for i in range(len(s)):
        t = s
        for j in range(i):
            t = t[1:] + t[0]
        prevT = ''
        while prevT != t:
            prevT = t
            for c in check:
                t = t.replace(c, '')
        if t == '':
            correct += 1
    return correct