def solution(N, stages):
    fail={}
    stack=0
    for i in range(1,N+1):
        fail[i]= 0 if stages.count(i) == 0 else (stages.count(i)/(len(stages)-stack))
        stack += stages.count(i)
    return sorted(range(1,len(fail)+1), key=lambda k: fail[k], reverse=True)