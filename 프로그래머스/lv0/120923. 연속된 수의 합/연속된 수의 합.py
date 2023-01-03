def solution(num, total):
    ans = []
    c = total // num
    ans.append(c)
    for i in range(1, num//2 + 1):
            if num % 2 == 0:
                if i < num // 2:
                    ans.insert(0, c - i)
            else:
                ans.insert(0, c - i)
            ans.append(c + i)
    return ans