from collections import deque

def solution(A,B):
    A = deque(sorted(A))
    B = deque(sorted(B))
    answer = 0
    while len(A) > 0:
        answer += A[-1] * B[0]
        A.pop()
        B.popleft()
    return answer