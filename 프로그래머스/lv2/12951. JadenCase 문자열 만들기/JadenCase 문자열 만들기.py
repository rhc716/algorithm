def solution(s):
    return ' '.join(list(map(lambda x:x.capitalize(), s.lower().split(' '))))