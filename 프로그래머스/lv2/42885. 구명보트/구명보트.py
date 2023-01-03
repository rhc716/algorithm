from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    cnt = 0
    while len(people) > 0:
        if len(people) > 1 and people[0] + people[-1] > limit:
            people.pop()
            cnt += 1
        elif len(people) > 1 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1
        else:
            people.pop()
            cnt += 1
    return cnt