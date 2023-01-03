import re

def solution(s):
    arr = sorted([re.sub('[{|}]', '', e)  for e in s.split("},{")], key=len)
    res = []
    for i in range(0, len(arr)):
        res.extend([e for e in arr[i].split(",") if e not in res])
    return list(map(int, res))