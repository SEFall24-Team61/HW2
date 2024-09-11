from hw2_debugging import merge_sort

def test_random_sorted_array():
    array = [27,10,1,14,4,58]
    expected_sorted_array = [1,4,10,14,27,58]
    actual_sorted_array = merge_sort(array)
    assert actual_sorted_array == expected_sorted_array

def test_sorted_asc_array():
    array = [4,15,18,23,35,41]
    expected_sorted_array = [4,15,18,23,35,41]
    actual_sorted_array = merge_sort(array)
    assert actual_sorted_array == expected_sorted_array