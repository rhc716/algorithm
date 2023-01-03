def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        end = False;
        while end == False:
            for c in can:
                if b.startswith(c+c):
                    end = True
                    break
            else:
                for c in can:
                    if b.startswith(c):
                        b = b[len(c):]
                        break
                else:
                    if b == '':
                        cnt += 1
                    end = True
    return cnt