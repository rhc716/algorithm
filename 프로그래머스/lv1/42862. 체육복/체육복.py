def solution(n, lost, reserve):
    re = set(reserve)-set(lost)
    lo = set(lost)-set(reserve)
    for i in re:
        if i-1 in lo:
            lo.remove(i-1)
        elif i+1 in lo:
            lo.remove(i+1)
    return n-len(lo)