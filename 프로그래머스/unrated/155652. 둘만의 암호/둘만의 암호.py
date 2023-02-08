def solution(s, skip, index):
    rule = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in skip]
    return ''.join([rule[(rule.index(c) + index) % len(rule)] for c in s])