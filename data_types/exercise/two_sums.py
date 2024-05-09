"""
Given an array of integers nums 
and an integer target, return indices of the 
two numbers such that they add up to target.

using the hashtable logic
"""

import evaluate

def twoSum(nums, target: int):
    numDict = {}
    n = len(nums)
    
    for i in range(n):
        numDict[nums[i]] = i 
        
    for i in range(n):
        complement = target - nums[i]
        if complement in numDict and numDict[complement] != i:
            return [i, numDict[complement]]
            
    return []