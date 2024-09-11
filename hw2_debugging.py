"""
This module implements the merge sort algorithm.

It contains two main functions:
- mergeSort: Recursively splits and sorts an array.
- recombine: Merges two sorted arrays into a single sorted array.
"""
import rand


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new list containing all elements from arr in sorted order.
    """

    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Parameters:
    leftArr (list): The first sorted array.
    rightArr (list): The second sorted array.

    Returns:
    list: A new list containing all elements from leftArr and rightArr in sorted order.
    """

    left_index = 0
    right_index = 0
    merge_arr = []
    
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


random_array = rand.random_array([None] * 20)
sorted_array = merge_sort(random_array)

print(sorted_array)
