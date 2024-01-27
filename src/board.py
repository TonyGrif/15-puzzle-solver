"""This module contains the Board class structure"""

import logging
from typing import List

import numpy as np


class Board:
    """Class utilized for storing board state data and defining
    the actions that can be performed on the board.

    Variables:
        starting_state (np.ndarry): The starting point for this game.
    """

    def __init__(self, matrix_list: List) -> None:
        """The default constructor for a board object.

        Parameters:
            matrix_list (List): Single list containing the board data.
            The data is expected to contain the numbers 0-15 with a blank
            space represented by 0 and will not be validated within
            this class.
        """
        # Convert list to 4x4 matrix
        # Save beginning state
        # Add to a state tracker
        logging.debug("Row 1: %s", matrix_list[0:4])
        logging.debug("Row 2: %s", matrix_list[4:8])
        logging.debug("Row 3: %s", matrix_list[8:12])
        logging.debug("Row 4: %s", matrix_list[12:16])

        # TODO: Try list compressions to aid readability
        init_array = np.array(
            [matrix_list[0:4], matrix_list[4:8], matrix_list[8:12], matrix_list[12:16]]
        )

        self.starting_state = init_array
