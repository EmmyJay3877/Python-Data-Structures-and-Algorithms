"""
Merge Sort: The process of merge sort is to divide the 
array into two halves, sort each half, and then merge the sorted 
halves back together. This process is repeated until the entire array is sorted.
"""

def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[mid:]
        right_half = arr[:mid]

        #recursive call on the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        #merge the two sorted halves
        merge(arr, left_half, right_half)