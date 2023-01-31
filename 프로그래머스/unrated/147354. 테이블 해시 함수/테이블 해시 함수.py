def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: [x[col-1], -x[0]])      # 정렬 우선순위 col 오름차, 기본키 ([0]) 내림차
    res = 0
    for i in range(row_begin, row_end + 1):
        res ^= sum(map(lambda x: x % i, data[i-1])) # S_i 구해서 누적 ^= (XOR) 연산
    return res