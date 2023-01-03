ans = 0
def solution(numbers, target):
    def dfs(i, n, arr):
        global ans
        if i == len(arr):
            if n == target:
                ans += 1
            return
        dfs(i+1, n+arr[i], arr)
        dfs(i+1, n-arr[i], arr)
    dfs(0, 0, numbers)
    return ans