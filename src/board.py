"""This module contains the Board class structure"""

import logging
from typing import List

import numpy as np


class Board:
    """Class utilized for storing board state data and defining
    the actions that can be performed on the board.

    Variables:
        starting_state (np.ndarray): The starting point for this game.
        goal_state (np.ndarray): The end goal to reach for this game.
    """

    def __init__(self, matrix_list: List) -> None:
        """The default constructor for a board object.

        Parameters:
            matrix_list (List): Single list containing the board data.
            The data is expected to contain the numbers 0-15 with a blank
            space represented by 0 and will not be validated within
            this class.
        """
        logging.debug("Row 1: %s", matrix_list[0:4])
        logging.debug("Row 2: %s", matrix_list[4:8])
        logging.debug("Row 3: %s", matrix_list[8:12])
        logging.debug("Row 4: %s", matrix_list[12:16])

        # TODO: Try list compressions to aid readability
        init_array = np.array(
            [matrix_list[0:4], matrix_list[4:8], matrix_list[8:12], matrix_list[12:16]]
        )

        self.starting_state = init_array
        self.goal_state = np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        )

    def move(self) -> None:
        """Move and swap the elements in a valid way.

        Parameters:
            TBW
        Returns:
            TBW
        """
        pass
