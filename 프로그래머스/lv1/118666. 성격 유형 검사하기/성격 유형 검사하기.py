def solution(survey, choices):
    scores = {'R': 0, 'T': 0,
              'C': 0, 'F': 0,
              'J': 0, 'M': 0,
              'A': 0, 'N': 0}
    answer = ''
    
    for s, c in zip(survey, choices):
        if c > 4:
            scores[s[1]] += c - 4
        elif c < 4:
            scores[s[0]] += 4 - c
    
    i = 0
    beforeKV = []
    for k, v in scores.items():
        if i % 2 == 1:
            if beforeKV[1] >= v:
                answer += beforeKV[0]
            else:
                answer += k
        beforeKV = [k, v]
        i += 1
    return answer