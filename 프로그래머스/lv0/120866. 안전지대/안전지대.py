def marking(mat, mines):
    for i, j in mines:
        if i-1 >= 0:
            mat[i-1][j] = -1
            if j-1 >= 0:
                mat[i-1][j-1] = -1
            if j+1 < len(mat[i]):
                mat[i-1][j+1] = -1
        mat[i][j] = -1
        if j-1 >= 0:
            mat[i][j-1] = -1
        if j+1 < len(mat[i]):
            mat[i][j+1] = -1
        if i+1 < len(mat):
            mat[i+1][j] = -1
            if j-1 >= 0:
                mat[i+1][j-1] = -1
            if j+1 < len(mat[i]):
                mat[i+1][j+1] = -1

def solution(board):
    mines = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                mines.append([i,j])
    marking(board, mines)
    return len(board) * len(board) + sum(sum(board,[]))