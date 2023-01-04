def solution(my_string):
    return sum(list(map(lambda x: int(x) if x.isnumeric() else 0, my_string)))