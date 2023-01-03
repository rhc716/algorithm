
def solution(h, w, board):
    # 리스트로 변환
    board = [list(s) for s in board]
    # 4블록 탐색 및 삭제 위치 기록
    def findDelPos():
        delPos = []
        for i in range(h-1):
            for j in range(w-1):
                if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    delPos.append([i,j])
        return delPos
    # 삭제 위치가 있으면
    while delPos := findDelPos():
        # 없앤다 = ' ' 넣기
        for d in delPos:
            i, j = d
            board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1] = ' '*4
        # 빈칸을 채운다
        for i in range(h-1, -1, -1):
            for j in range(w):
                if board[i][j] == ' ':
                    k = 1
                    while i-k >= 0 and board[i-k][j] == ' ':
                        k += 1
                    if i-k >= 0:
                        board[i][j] = board[i-k][j]
                        board[i-k][j] = ' '
    return sum(b.count(' ') for b in board)