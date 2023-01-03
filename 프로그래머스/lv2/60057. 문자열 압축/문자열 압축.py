def solution(s):
    result = []
    for i in range(1, len(s)//2+1):
        tmp=''
        count=1
        word=s[:i]
        for j in range(i, len(s)+i, i):
            if word==s[j:j+i]:
                count+=1
            else:
                tmp+=(str(count) if count>1 else '')+word
                word=s[j:j+i]
                count=1
        result.append(len(tmp))
    return 1 if not result else min(result)