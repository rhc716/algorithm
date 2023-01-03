def solution(n):
    base=['1','2','4']
    tmp=''
    while n:
        n,mod=divmod(n-1,3)
        tmp=base[mod]+tmp
    return tmp