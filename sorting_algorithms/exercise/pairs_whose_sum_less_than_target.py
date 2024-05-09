"""
Given a 0-indexed integer array nums of length n and 
an integer target, return the number of pairs (i, j) 
where 0 <= i < j < n and nums[i] + nums[j] < target.
"""

def count_pairs(nums, target):
    pairs = 0
    nums.sort()
    p1, p2 = 0, len(nums) - 1

    while p1 < p2:
        if nums[p1] + nums[p2] < target:
            pairs += p2 - p1
            p1 += 1
        else:
            p2 -= 1
    return pairs
