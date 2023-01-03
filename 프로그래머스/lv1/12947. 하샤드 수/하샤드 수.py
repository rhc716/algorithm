def solution(x):
    return x%sum([int(y) for y in str(x)])==0