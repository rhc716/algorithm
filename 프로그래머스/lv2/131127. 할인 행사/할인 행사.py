def solution(want, number, discount):
    result = 0
    for i in range(len(discount) - 9):
        for w, n in zip(want, number):
            if discount[i:i+10].count(w) < n:
                break
        else:
            result += 1
    return result