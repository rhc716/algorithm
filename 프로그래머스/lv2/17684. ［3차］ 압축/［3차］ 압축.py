def solution(msg):
    d_comp = { chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    result = []
    buff = ''
    i = 0
    while i < len(msg):
        buff += msg[i]
        if buff in d_comp:
            i += 1
        else:
            result.append(d_comp[buff[:-1]])
            d_comp[buff] = max(d_comp.values()) + 1
            buff = ''
    if buff: result.append(d_comp[buff])
    return result