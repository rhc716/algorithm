def solution(n, arr1, arr2):
    return [format(x|y,'b').zfill(n).translate(str.maketrans('01', ' #')) for x,y in zip(arr1, arr2)]