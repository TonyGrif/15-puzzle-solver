"""This module contains utility functions for the 15-puzzle solver.
"""

import logging
from typing import List


def convert_string_to_list(matrix_string: str) -> List:
    """Convert the input string to a list to be converted later.

    Parameters:
        matrix_string (str): The input string to be converted.

    Returns:
        A list containing the string data.
    """
    # TODO: Clean this up a little
    matrix_list = matrix_string.split(" ")
    matrix_list = [char for char in matrix_list if char]

    for indx, item in enumerate(matrix_list):
        if item == "_":
            matrix_list[indx] = 0
        else:
            matrix_list[indx] = int(item)

    logging.debug("%s: %s", type(matrix_list), matrix_list)
    return matrix_list


def validate_list(matrix_list: List) -> bool:
    """Validates the list to ensure the program can be started with the
    provided state

    Parameters:
        matrix_list (List): The list of characters to be analyzed.

    Throws:
        Assertion error for wrong number of character or improper
        numbers provided.

    Returns:
        Return True if the above checks are passed, throw an above
        exception otherwise.
    """
    if len(matrix_list) != 16:
        raise AssertionError(
            "Invalid number of characters provided (expect 1-15 & '_' character)."
        )

    for num in range(0, 16):
        if num not in matrix_list:
            raise AssertionError("Invalid number input (expect 1-15 & '_' character).")

    return True
