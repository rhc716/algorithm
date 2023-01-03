def solution(polynomial):
    sp = polynomial.split(' + ')
    ax, b = 0, 0
    for s in sp:
        if 'x' in s:
            if 'x' == s:
                ax += 1
            else:
                ax += int(s.replace('x', ''))
        else:
            b += int(s)
    ax = '' if ax == 0 else 'x' if ax == 1 else str(ax) + 'x'
    b = '' if b == 0 else ('' if ax == '' else ' + ') + str(b)
    return ax + b