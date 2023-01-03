def solution(array, n):
    array.sort()
    t = [abs(x - n) for x in array]
    return array[t.index(min(t))]