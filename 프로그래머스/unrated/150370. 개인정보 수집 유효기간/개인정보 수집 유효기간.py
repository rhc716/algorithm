from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    fm_date = "%Y.%m.%d"
    today = datetime.strptime(today, fm_date)
    terms = {t[0]:int(t[2:]) for t in terms}
    res = []
    for i, v in enumerate(privacies):
        pdate = datetime.strptime(v[0:-2], fm_date) + relativedelta(months=terms[v[-1:]])
        if pdate <= today:
            res.append(i+1)
    return res