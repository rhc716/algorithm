import numpy as np

def solution(n, t, m, p):
    speak = ""
    end = (t-1)*m+p
    i = 0
    while len(speak) < end:
        speak += np.base_repr(i, base=n)
        i += 1
    return speak[p-1:end:m]