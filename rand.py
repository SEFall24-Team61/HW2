"""
This module provides a function to generate a shuffled random array of integers.

The function `random_array` fills the provided list with integers between 1 and 20 randomly.
"""
import subprocess


def random_array(arr):
    """
    Fills the provided list with random integers between 1 and 20.

    Parameters:
    arr (list): The list to be filled with random integers.

    Returns:
    list: The input list with each element replaced by a random integer between 1 and 20.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout.strip())
    return arr
