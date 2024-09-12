"""
This module contains tests for the merge_sort function
from the hw2_debugging module.
"""

from hw2_debugging import merge_sort

def test_random_sorted_array():
    """
    Tests merge_sort with an unsorted array and checks if the output is correctly sorted.
    """
    array = [27,10,1,14,4,58]
    expected_sorted_array = [1,4,10,14,27,58]
    actual_sorted_array = merge_sort(array)
    assert actual_sorted_array == expected_sorted_array

def test_sorted_asc_array():
    """
    Tests merge_sort with an already sorted array in ascending order.
    """
    array = [4,15,18,23,35,41]
    expected_sorted_array = [4,15,18,23,35,41]
    actual_sorted_array = merge_sort(array)
    assert actual_sorted_array == expected_sorted_array

def test_sorted_desc_array():
    """
    Tests merge_sort with an array sorted in descending order
    and checks if the output is correctly sorted in ascending order.
    """
    array = [91,45,32,17,8,3]
    expected_sorted_array = [3,8,17,32,45,91]
    actual_sorted_array = merge_sort(array)
    assert actual_sorted_array == expected_sorted_array
