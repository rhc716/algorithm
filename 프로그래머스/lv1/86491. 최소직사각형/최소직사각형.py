def solution(sizes):
    # 모든 사각형의 긴쪽을 바닥으로 해서 눕혔다고 가정
    # 바닥으로 눕힌 길이 들 중에서 가장 큰 값
    # 세운 길이에서 가장 큰 값
    # 두 수의 곱
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)