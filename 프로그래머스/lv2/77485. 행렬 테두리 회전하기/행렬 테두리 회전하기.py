import numpy as np

def solution(rows, cols, quer):
    mins = []
    mat = np.array(range(1, rows*cols+1)).reshape(rows, cols)
    for q in quer:
        width = q[3]-q[1]+1
        height = q[2]-q[0]+1
        t_arr = [mat[q[0]-1][q[1]-1]]
        # →
        for i in range(1, width):
            t_arr.append(mat[q[0]-1][q[1]-1+i])
            mat[q[0]-1][q[1]-1+i] = t_arr[-2]
        # ↓
        for i in range(1, height):
            t_arr.append(mat[q[0]-1+i][q[3]-1])
            mat[q[0]-1+i][q[3]-1] = t_arr[-2]
        # ←
        for i in range(1, width):
            t_arr.append(mat[q[2]-1][q[3]-1-i])
            mat[q[2]-1][q[3]-1-i] = t_arr[-2]
        # ↑
        for i in range(1, height):
            t_arr.append(mat[q[2]-1-i][q[1]-1])
            mat[q[2]-1-i][q[1]-1] = t_arr[-2]
        mins.append(int(min(t_arr)))
    return mins