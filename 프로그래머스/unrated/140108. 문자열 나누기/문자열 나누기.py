def solution(s):
    s = list(s)
    res = []
    while s:
        x = s.pop(0)
        cnt_x, cnt_else = 1, 0
        buff = x
        while s:
            c = s.pop(0)
            if c == x:
                cnt_x += 1
            else:
                cnt_else += 1
            buff += c
            if cnt_x == cnt_else:
                res.append(buff)
                buff = ''
                break
    return len(res) + (1 if buff else 0)