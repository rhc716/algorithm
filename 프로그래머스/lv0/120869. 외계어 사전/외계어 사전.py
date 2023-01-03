def solution(spell, dic):
    for d in dic:
        if len({s : d.count(s) for s in spell if d.count(s) == 1}) == len(spell):
            return 1
    return 2