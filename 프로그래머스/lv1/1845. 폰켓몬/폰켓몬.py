def solution(nums):
    return int(len(nums)/2) if len(nums)/2 <= len(set(nums)) else len(set(nums))