def solution(name):
    ud = [min([abs(ord('A') - ord(c)), abs(ord('Z') - ord(c))+1]) for c in name]
    udMove = sum(ud)
    ud[0] = 0
    lr = []
    def dfs(arr, i, moves):
        if set(arr) == {0}:
            lr.append(moves)
            return
        for j in range(1, len(arr)):
            if arr[i+j] != 0:
                tmp = arr.copy()
                tmp[i+j] = 0
                dfs(tmp, i+j, moves+j)
                break
        for j in range(1, len(arr)):
            if arr[i-j] != 0:
                tmp = arr.copy()
                tmp[i-j] = 0
                dfs(tmp, i-j, moves+j)
                break
    dfs(ud, 0, 0)
    return udMove + min(lr)