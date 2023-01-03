def solution(s):
    stack = [0]
    for c in s:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 1 if stack == [0] else 0