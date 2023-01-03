def solution(s):
    slen = len(s)
    return s[slen//2-1]+s[slen//2] if slen%2 == 0 else s[slen//2]