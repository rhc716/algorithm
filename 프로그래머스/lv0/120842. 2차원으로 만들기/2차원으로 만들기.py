def solution(num_list, n):
    answer = []
    tmp = []
    for i, v in enumerate(num_list):
        tmp.append(v)
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
    return answer