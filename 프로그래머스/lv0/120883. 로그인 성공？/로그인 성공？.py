def solution(id_pw, db):
    db = dict(db)
    if id_pw[0] in db:
        if id_pw[1] == db[id_pw[0]]:
            return 'login'
        else:
            return 'wrong pw'
    return 'fail'