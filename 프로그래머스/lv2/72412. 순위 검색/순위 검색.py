import bisect, collections, itertools

def solution(info, query):
    res = [0] * len(query)
    dic = collections.defaultdict(list)
    hyphen = [h for h in itertools.product([True, False], repeat=4)]
    for inf in info:
        sp = inf.split()
        for hy in hyphen:
            key = ''.join(['-' if hy[i] else sp[i] for i in range(4)])
            dic[key].append(int(sp[4]))
    for k in dic:
        dic[k].sort()
    for i, q in enumerate(query):
        key, score = q.replace(' and ', '').split()
        res[i] = len(dic[key]) - bisect.bisect_left(dic[key], int(score))
    return res