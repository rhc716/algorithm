def solution(record):
    answer = []
    names = {}
    for x in record:
        if 'Enter' in x or 'Change' in x:
            xp = x.split(' ')
            names[xp[1]] = xp[2]
    for x in record:
        xp = x.split(' ')
        if 'Enter' in x:
            answer.append('{}님이 들어왔습니다.'.format(names[xp[1]]))
        elif 'Leave' in x:
            answer.append('{}님이 나갔습니다.'.format(names[xp[1]]))
    return answer