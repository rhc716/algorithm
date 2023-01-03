def solution(board, moves):
    selected = [0]
    boom = 0
    for x in moves:
        for row in board:
            if row[x-1] != 0:
                selected.append(row[x-1])
                row[x-1] = 0
                if selected[-1] == selected[-2]:
                    selected.pop(-1)
                    selected.pop(-1)
                    boom += 2
                break
    return boom