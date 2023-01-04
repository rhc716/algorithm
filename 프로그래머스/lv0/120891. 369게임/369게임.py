def solution(order):
    order = str(order)
    cnt = order.count('3')
    cnt += order.count('6')
    cnt += order.count('9')
    return cnt