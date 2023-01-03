def solution(arr):
    return [-1] if len(arr) == 1 else arr.pop(arr.index(min(arr))) and arr