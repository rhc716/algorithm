import math

def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    tmp = days[0]
    cnt = 0
    ans = []
    for d in days:
        if tmp<d:
            ans.append(cnt)
            tmp = d
            cnt = 0
        cnt += 1
    ans.append(cnt)
    return ans