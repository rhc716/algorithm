from collections import deque

def solution(ingredient):
    dq = deque()
    cnt = 0
    for i in ingredient:
        dq.append(i)
        if len(dq) >= 4:
            if [1, 2, 3, 1] == [dq[-4], dq[-3], dq[-2], dq[-1]]:
                dq.pop()
                dq.pop()
                dq.pop()
                dq.pop()
                cnt += 1
    return cnt