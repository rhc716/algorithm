def solution(n, words):
    sp = [ words[i:i+n] for i in range(0, len(words), n) ]
    said = []
    prevW = sp[0][0][0]
    for i, v in enumerate(sp):
        for j, w in enumerate(v):
            if w in said or prevW[-1] != w[0]:
                return [j+1, i+1]
            said.append(w)
            prevW = w
    return [0, 0]