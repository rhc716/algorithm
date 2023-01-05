def counter(n, idx):
    ret = 0
    for i in range(n, 0, -1):
        if i == 1:
            return ret + '11011'[0:idx].count('1')
        else:
            # n번째 칸토어 비트에서 1의 갯수를 구하려
            # 프랙탈 구조이므로, 상위 차원에서 하위차원으로 idx를 기준으로 점점 세어감
            # [ 프렉탈 구조 : (하위 + 하위) + ('0' * 5 ** n-1) + (하위 + 하위) ] 크게 3 부분으로 구분
            cnt_all = 5 ** (i - 1)
            cnt_1 = 4 ** (i - 1)
            if idx <= 2 * cnt_all:
                ret += cnt_1 * (idx // cnt_all)
                idx = idx % cnt_all
            elif idx > 3 * cnt_all:
                ret += cnt_1 * (2 + (idx - 3 * cnt_all) // cnt_all)
                idx = (idx - 3 * cnt_all) % cnt_all
            else:
                return ret + cnt_1 * 2

def solution(n, l, r):
    return counter(n, r) - counter(n, l-1)