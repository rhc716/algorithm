def solution(left, right):
    return sum([x if sum([1 if x%i==0 else 0 for i in range(1, x+1)])%2==0 else -x for x in range(left, right+1)])