"""
Bubble Sort: A sorting algorithm that compares two adjacent
elements and swaps them until they are in the intendend order.

In the code below, the outer loop is responsible for controlling 
number of interations over the entire list while the inner loop
is responsible for comparing and swapping adjacent 
elements within the unsorted portion of the list
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n): 
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
