def solution(s):
    slist = []
    for x in s.split(' '):
        x = list(x.lower())
        for i in range(len(x)):
            if i%2==0:
                x[i] = x[i].upper()
        slist.append(''.join(x))
    return ' '.join(slist)