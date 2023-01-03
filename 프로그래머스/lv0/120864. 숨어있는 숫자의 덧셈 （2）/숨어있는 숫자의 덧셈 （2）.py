import re

def solution(s):
    return sum(list(map(lambda x: int(x) if x!= '' else 0, re.split('[A-z]', s))))