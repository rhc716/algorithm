def solution(food):
    t = ''.join([str(i+1) * (v//2) for i, v in enumerate(food[1:])])
    return t + '0' + t[::-1]