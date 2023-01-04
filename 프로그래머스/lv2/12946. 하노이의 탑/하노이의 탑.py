def solution(n):
    def move(num, _from, _through, _to):
        if num == 1:
            return [[_from, _to]]
        return move(num-1, _from, _to, _through) + [[_from, _to]] + move(num-1, _through, _from, _to)
    return move(n, 1, 2, 3)