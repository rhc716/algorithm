import numpy as np

def solution(numbers, hand):
    base = np.array([['1','4','7','*'],['2','5','8','0'],['3','6','9','#']])
    L = '*'; R = '#'
    answer = ''
    
    for x in numbers:
        x = str(x)
        pX = np.concatenate(np.where(base == x));
        pL = np.concatenate(np.where(base == L));
        pR = np.concatenate(np.where(base == R));
        distL = abs(pX[0] - pL[0]) + abs(pX[1] - pL[1])
        distR = abs(pX[0] - pR[0]) + abs(pX[1] - pR[1])
        
        if pX[0] == 0 or (pX[0] == 1 and distL < distR):
            L = x; answer += 'L'
        elif pX[0] == 2 or (pX[0] == 1 and distL > distR):
            R = x; answer += 'R'
        else:
            if hand == 'left':
                L = x; answer += 'L'
            else:
                R = x; answer += 'R'
    return answer