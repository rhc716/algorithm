def solution(elements):
    sums = set()
    for i in range(1, len(elements)+1):
        tmp = elements[len(elements)-i+1:len(elements)] + elements
        for j in range(0, len(tmp)-i+1):
            sums.add(sum(tmp[j:j+i]))
    return len(sums)