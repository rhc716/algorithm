def solution(chicken):
    if chicken >= 10:
        return chicken//10 + solution(chicken//10+chicken%10)
    return 0