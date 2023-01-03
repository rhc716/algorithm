def solution(ab, si):
    for i in range(len(ab)):
        ab[i] = ab[i] if si[i] else -ab[i]
    return sum(ab)