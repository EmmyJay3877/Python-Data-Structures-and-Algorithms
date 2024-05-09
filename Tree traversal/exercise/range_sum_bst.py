
"""
Given the root node of a binary search tree and 
two integers low and high, return the sum of values of 
all nodes with a value in the inclusive range [low, high].
"""

def range_sum_bst(root, low, high):
    if root is None:
        return 0
    if root.val > high:
        return range_sum_bst(root.left, low, high)
    elif root.val < low:
        return range_sum_bst(root.right, low, high)
    total_sum = root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)
    return total_sum
