import numpy as np

def solution(arr1, arr2):
    return (np.matrix(arr1) * np.matrix(arr2)).tolist()