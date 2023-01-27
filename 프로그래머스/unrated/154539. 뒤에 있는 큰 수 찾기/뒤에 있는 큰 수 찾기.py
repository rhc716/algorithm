from heapq import heapify, heappush, heappop

def solution(numbers):
    answer = [-1 for _ in numbers] # -1 (못찾음) 로 초기화
    hq = []
    heapify(hq)
    for i, v in enumerate(numbers):
        while hq and hq[0][0] < v: # 현재 나온 값보다 스택의 top이 작을때, answer에 값 변경
            answer[heappop(hq)[1]] = v
        heappush(hq, (v, i))       # 가장 작은 값이 top으로 오도록
    return answer