"""
Linear Search: it examines each element from one end to the other end until it finds a match
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            # Target found, return the index
            return i

    # Target not found in the array
    return -1
