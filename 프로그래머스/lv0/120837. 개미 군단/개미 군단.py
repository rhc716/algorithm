def solution(hp):
    a, hp = divmod(hp, 5)
    b, hp = divmod(hp, 3)
    return a+b+hp