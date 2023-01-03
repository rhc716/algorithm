def solution(s, n):
    ABC = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    abc = [chr(x) for x in range(ord('a'), ord('z')+1)]
    ans = ''
    for c in s:
        if c in ABC:
            ans += ABC[(ABC.index(c) + n)%len(ABC)]
        elif c in abc:
            ans += abc[(abc.index(c) + n)%len(abc)]
        else:
            ans += c
    return ans