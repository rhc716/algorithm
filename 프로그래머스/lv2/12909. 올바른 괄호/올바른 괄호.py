def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    l,r=0,0
    for c in s:
        if c == '(':
            l+=1
        else:
            r+=1
        if r>l:
            return False
    return True if l==r else False