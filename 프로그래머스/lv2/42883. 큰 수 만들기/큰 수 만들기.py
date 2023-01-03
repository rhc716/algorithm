def solution(number, k):
    res = ""
    res_len = len(number) - k
    while True:
        for i in range(9, -1, -1):
            f = number.find(str(i))
            if -1 < f <= k:
                res += number[f]
                number = number[f+1:]
                k -= f
                if k == 0:
                    return res + number
                elif len(res) == res_len:
                    return res
                break