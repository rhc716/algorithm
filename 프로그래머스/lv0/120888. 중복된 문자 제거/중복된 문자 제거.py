def solution(my_string):
    ans = ''
    for c in my_string:
        if not c in ans:
            ans += c
    return ans