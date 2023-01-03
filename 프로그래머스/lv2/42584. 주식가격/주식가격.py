def solution(prices):
    result = [0] * len(prices)
    for i, v in enumerate(result):
        j = i + 1
        while j < len(prices):
            result[i] += 1
            if prices[j] >= prices[i]:
                j += 1
            else:
                break
    return result