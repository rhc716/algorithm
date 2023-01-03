def solution(t, p):
    lp = len(p)
    ip = int(p)
    cnt = 0
    for i in range(len(t) - lp + 1):
        if int(t[i:i+lp]) <= ip:
            cnt += 1
    return cnt