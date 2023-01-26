def solution(k, ranges):
    seq = [k]  # 우박 수열 만들기
    while k > 1:
        k = k // 2 if k % 2 == 0 else k * 3 + 1
        seq.append(k)
    areas = [] # 구간별 넓이 구하기
    for a, b in zip(seq, seq[1:]):
        areas.append((a + b) / 2)
    res = []   # 정적분 = 주어진 구간의 넓이
    for start, e in ranges:
        end = len(seq) + e - 1
        if start == end:
            res.append(0.0)
        elif start > end:
            res.append(-1.0)
        else:
            res.append(sum(areas[start:end]))
    return res