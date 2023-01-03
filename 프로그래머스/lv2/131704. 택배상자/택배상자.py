from collections import deque

def solution(order):
    order = deque(order)
    belt1 = deque(range(1, len(order) + 1))
    belt2 = deque([-1])
    cnt = 0
    while len(order) > 0:
        if len(belt1) > 0 and order[0] == belt1[0]:
            cnt += 1
            belt1.popleft()
            order.popleft()
        elif order[0] == belt2[-1]:
            cnt += 1
            belt2.pop()
            order.popleft()
        else:
            if len(belt1) > 0:
                belt2.append(belt1.popleft())
            else:
                break
    return cnt