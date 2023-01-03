from itertools import combinations

def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def solution(nums):
    return sum([isPrime(s) for s in [sum(x) for x in list(combinations(nums, 3))]])