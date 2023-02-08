from datetime import datetime

def solution(book_time):
    board = [0] * 1450
    for time in book_time:
        start, end = datetime.strptime(time[0], "%H:%M"), datetime.strptime(time[1], "%H:%M")
        start, end = start.hour * 60 + start.minute, end.hour * 60 + end.minute
        for i in range(start, end + 10):
            board[i] += 1
    return max(board)

# 예약 시간의 범위를 board 에 계속 겹쳐서 최고층 (가장 많이 겹친 층) 을 구하면 됨
# 00:00 ~ 23:59 까지 : 1440 + 10 분 ( board의 청소시간 패딩 값 )
# 퇴실 시간 + 10분 => 10 분 청소시간