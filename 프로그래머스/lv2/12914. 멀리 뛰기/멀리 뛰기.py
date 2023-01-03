def solution(n):
    arr = [1,2]
    while len(arr) < n:
        arr.append(arr[-2]+arr[-1])
    return arr[n-1]%1234567