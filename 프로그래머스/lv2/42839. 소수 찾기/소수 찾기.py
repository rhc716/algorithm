from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    tmp = set()
    for i in range(1,len(numbers)+1):
        for arr in set(permutations(numbers, i)):
            x = int(''.join(arr))
            if is_prime(x) == True:
                tmp.add(x)
    return len(tmp)