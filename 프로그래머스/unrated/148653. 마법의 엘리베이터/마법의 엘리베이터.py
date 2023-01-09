def solution(storey):
    storey = list(map(int, str(storey)))
    res = []
    def dfs(i, carry, total):
        nonlocal res
        if i == -1:
            res.append(total + carry)
            return
        n = storey[i] + carry
        dfs(i - 1, 0, total + n)
        dfs(i - 1, 1, total + 10 - n)
    dfs(len(storey) - 1, 0, 0)
    return min(res)