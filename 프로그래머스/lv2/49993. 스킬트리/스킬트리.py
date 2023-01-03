def solution(skill, skill_trees):
    findArr = [[st.find(k) for k in skill] for st in skill_trees]
    cnt = 0
    for f in findArr:
        for prev, curr in zip(f, f[1:]):
            if (prev == -1 and curr != -1) or (prev > curr and curr != -1):
                break
        else:
            cnt += 1
    return cnt