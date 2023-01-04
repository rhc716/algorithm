def solution(my_string):
    return list(map(int, [x for x in sorted(my_string) if x.isnumeric()]))