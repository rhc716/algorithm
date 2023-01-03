import re
from itertools import permutations

def solution(expression):
    ans = []
    for ops in list(permutations('+-*')):
        nbrs = re.split('\+|-|\*', expression)
        oprs = list(filter(None, re.split('\d+', expression)))
        print(nbrs, oprs, ops)
        for op in ops:
            while op in oprs:
                i = oprs.index(op)
                nbrs.insert(i+2, str(eval(nbrs[i] + op + nbrs[i+1])))
                del nbrs[i:i+2]
                del oprs[i]
        ans.append(abs(int(eval(nbrs[0]))))
    return max(ans)