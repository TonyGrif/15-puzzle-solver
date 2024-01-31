"""This module contains the Board class structure."""

import logging
from typing import List, Tuple

import numpy as np


class Board:
    """Class utilized for storing board state data and defining
    the actions that can be performed on the board.

    Variables:
        starting_state (np.ndarray): The starting point for this game.
        current_state (np.ndarray): The current state of this game.
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

        self.current_state = init_array
        self.goal_state = np.array(
            [
                ["1", "2", "3", "4"],
                ["5", "6", "7", "8"],
                ["9", "10", "11", "12"],
                ["13", "14", "15", "_"],
            ]
        )

    def __str__(self) -> str:
        """Return a string representation of the current state for
        printing to console.

        Returns:
            Formatted string representation of the current state.
        """
        string = "|" + ("-" * 16) + "|\n"

        for rows in self.current_state:
            string += "|"
            for elem in rows:
                string += f"{elem: <4}"
            string += "|\n"

        string += "|" + ("-" * 16) + "|\n"
        return string

    def move(self, move: str) -> bool:
        """Swap the elements and update the current state.

        Parameters:
            move (str): The direction to move in. Up", "Down",
            "Left", and "Right" are the valid options.

        Returns:
            True if the move was successful, False otherwise.
        """
        if move not in self.get_valid_moves():
            return False

        row, col = self._get_blank_spot()

        if move == "Up":
            self.current_state[row][col], self.current_state[row + 1][col] = (
                self.current_state[row + 1][col],
                self.current_state[row][col],
            )
        if move == "Down":
            self.current_state[row][col], self.current_state[row - 1][col] = (
                self.current_state[row - 1][col],
                self.current_state[row][col],
            )

        if move == "Left":
            self.current_state[row][col], self.current_state[row][col - 1] = (
                self.current_state[row][col - 1],
                self.current_state[row][col],
            )
        if move == "Right":
            self.current_state[row][col], self.current_state[row][col + 1] = (
                self.current_state[row][col + 1],
                self.current_state[row][col],
            )

        return True

    def get_valid_moves(self) -> Tuple[str]:
        """Return the valid moves given the current state.

        Returns:
            A tuple containing the valid moves. This will contain two or more
            directions the board can shift in the form of strings.
        """
        row, col = self._get_blank_spot()
        moves = []

        if row != 3:
            moves.append("Up")
        if row != 0:
            moves.append("Down")

        if col != 0:
            moves.append("Left")
        if col != 3:
            moves.append("Right")

        return tuple(moves)

    def is_goal_state(self) -> bool:
        """Determine if the goal state has been reached.

        Returns:
            True if the current state is equal to the goal state,
            False otherwise.
        """
        return np.array_equal(self.current_state, self.goal_state)

    def _get_blank_spot(self) -> Tuple[int]:
        """Get the location of the blank space.

        Returns:
            Two-dimensional tuple containing the indices of the blank.
        """
        row, col = np.where(self.current_state == "_")
        return (row[0], col[0])
