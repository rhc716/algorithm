from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    avg = (sum(queue1)+sum(queue2))/2
    rg = (len(queue1)+len(queue2))*2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if avg%1 == 0:
        for i in range(rg):
            if sum1 < sum2:
                tmp = queue2.popleft()
                queue1.append(tmp)
                sum1 += tmp
                sum2 -= tmp
            elif sum1 > sum2:
                tmp = queue1.popleft()
                queue2.append(tmp)
                sum2 += tmp
                sum1 -= tmp
            else:
                return i
        return -1
    else:
        return -1