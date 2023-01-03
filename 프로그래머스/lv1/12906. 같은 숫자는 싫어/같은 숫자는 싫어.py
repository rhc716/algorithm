def solution(arr):
    tmp = []
    for x in arr:
        if tmp and tmp[-1] == x:
            continue
        tmp.append(x)
    return tmp