def solution(brown, yellow):
    divisors = [i for i in range(3, (brown + yellow)//2 + 1) if (brown + yellow) % i == 0]
    for w in divisors:
        for h in divisors:
            if (w - 2) * (h - 2) == yellow:
                return [max([w, h]), min([w, h])]
    return 0