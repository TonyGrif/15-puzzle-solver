"""This module contains the Board class structure"""

from typing import List


class Board:
    """Class utilized for storing board state data and defining
    the actions that can be performed on the board.

    Variables:
        TBW
    """

    def __init__(self, full_list: List) -> None:
        """The default constructor for a board object.

        Parameters:
            full_list (List): Single list containing the board data.
            The data is expected to contain the numbers 0-15 with a blank
            space represented by '_' and will not be validated within
            this class.
        """
        # Convert list to 4x4 matrix
        # Save beginning state
        # Add to a state tracker
        pass
