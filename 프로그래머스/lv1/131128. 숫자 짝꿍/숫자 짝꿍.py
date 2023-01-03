from collections import Counter

def solution(X, Y):
    tmp = ''
    for k, v in (Counter(X) & Counter(Y)).items():
        tmp += k * v
    if tmp == '':
        return '-1'
    elif tmp[0] == '0':
        return '0'
    tmp = ''.join(sorted(tmp, key=lambda x: -int(x)))
    return tmp