from collections import Counter

def solution(s1, s2):
    A = [s1[i:i+2].upper() for i in range(len(s1)-1) if s1[i:i+2].isalpha()]
    B = [s2[i:i+2].upper() for i in range(len(s2)-1) if s2[i:i+2].isalpha()]
    inter = sum((Counter(A) & Counter(B)).values())
    uni = sum((Counter(A) | Counter(B)).values())
    if inter == uni:
        return 65536
    return int(inter/uni * 65536)