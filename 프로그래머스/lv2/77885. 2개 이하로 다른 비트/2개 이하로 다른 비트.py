def solution(numbers):
    res = []
    for n in numbers:
        if n % 2 == 0:
            res.append(n+1)
        else:
            nbin = bin(n)[2:]
            if '01' in nbin:
                nbin = nbin[::-1].replace('10', '01', 1)[::-1]
            else:
                nbin = nbin.replace('1', '10', 1)
            res.append(int(nbin, 2))
    return res
