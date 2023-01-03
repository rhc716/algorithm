import numpy as np

def solution(keyinput, board):
    t = {'left' : [-1, 0], 'right' : [1, 0], 'up' : [0, 1], 'down': [0, -1]}
    me = np.array([0, 0])
    bo = np.array(board)//2
    for k in keyinput:
        if ((-bo <= me + t[k]) & (me + t[k] <= bo)).all():
            me += t[k]
    return me.tolist()