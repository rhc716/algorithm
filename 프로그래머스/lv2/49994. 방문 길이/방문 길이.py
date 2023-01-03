import numpy as np

def solution(dirs):
    T = {"U":(1, 0),"D":(-1,0),"L":(0,-1),"R":(0,1)}
    me = np.array((0, 0))
    log = set()
    for d in dirs:
        tmp = me + T[d]
        if -6 < tmp[0] < 6 and -6 < tmp[1] < 6:
            log.add((me[0],me[1],tmp[0],tmp[1]))
            log.add((tmp[0],tmp[1],me[0],me[1]))
            me = tmp
    return len(log)//2