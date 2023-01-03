from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        if a+b < b+a:
            return 1
        else:
            return -1
    newArr = sorted(list(map(str, numbers)), key=cmp_to_key(compare))
    return "0" if newArr[0] == '0' else ''.join(newArr)