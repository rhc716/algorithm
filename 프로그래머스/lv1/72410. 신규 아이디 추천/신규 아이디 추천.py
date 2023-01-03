import re

def solution(new_id):
    new_id = re.sub("\.+", ".", re.sub("[^\w\.\-\_]", "", new_id.lower())).strip(".")
    if new_id == "":
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15].strip(".")
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id