from collections import deque

def solution(A, B):
    d = deque(A)
    for i in range(0, len(A)):
        if ''.join(d) == B:
            return i
        d.rotate(1)
    return -1