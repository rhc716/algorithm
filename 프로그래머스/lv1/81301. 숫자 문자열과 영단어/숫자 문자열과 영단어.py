def solution(s):
    arr = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    while not(s.isnumeric()):
        for i in range(len(arr)):
            if arr[i] in s:
                s = s.replace(arr[i], str(i))
                break;
    return int(s)