from heapq import nsmallest

def solution(array, commands):
    return [max(nsmallest(c[2], array[c[0]-1:c[1]])) for c in commands]