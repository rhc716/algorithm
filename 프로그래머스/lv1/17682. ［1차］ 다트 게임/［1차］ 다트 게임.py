import re

def solution(dartResult):
    sdt = {'S' : 1, 'D' : 2, 'T': 3}
    p = re.compile('(\d+)([SDT])([*#]?)')
    arr = p.findall(dartResult)
    for i in range(len(arr)):
        num = pow(int(arr[i][0]), sdt[arr[i][1]])
        if '#' == arr[i][2]:
            num *= -1
        if '*' in arr[i][2]:
            num *= 2
            if i>0:
               arr[i-1] *= 2
        arr[i] = num
    return sum(arr)