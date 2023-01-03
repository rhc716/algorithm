def solution(p):
    def dfs(s):
        if s == '':
            return ''
        cnt, sp = 0, 0
        for i in range(len(s)):
            cnt += 1 if s[i] == s[0] else -1
            if i > 0 and cnt == 0:
                sp = i + 1
                break
        u, v = s[:sp], s[sp:]
        if u[0] == '(':
            return u + dfs(v)
        else:
            table = str.maketrans('()', ')(')
            return '(' + dfs(v) + ')' + u[1:-1].translate(table)
    return dfs(p)