def solution(bab):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in bab:
        for c in can:
            b = b.replace(c, '1', 1)
        if b.count('1') == len(b):
            cnt += 1
    return cnt