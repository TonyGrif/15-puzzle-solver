"""This module contains the Board class structure."""

from typing import List, Tuple


class Board:
    """Class utilized for storing board state data and defining
    the actions that can be performed on the board.

    Variables:
        current_state (List[List[str]]): The current state of this game.
        goal_state (List[List[str]]): The end goal to reach for this game.
    """

    def __init__(self, matrix_list: List[str]) -> None:
        """The default constructor for a board object.

        Parameters:
            matrix_list (List[str]): Single list containing the board data.
            The data is expected to contain the numbers 1-15 with a blank
            space represented by "_" and will not be validated within
            this class.
        """
        self._current_state = [
            matrix_list[x : x + 4] for x in range(0, len(matrix_list), 4)
        ]

        self._goal_state = [
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
            ["9", "10", "11", "12"],
            ["13", "14", "15", "_"],
        ]

    @property
    def current_state(self) -> List[List[str]]:
        """Get the current state of this board.

        Returns:
            Returns the 2d array representation of this board.
        """
        return self._current_state

    @property
    def goal_state(self) -> List[List[str]]:
        """Get the goal state of this board.

        Returns:
            Returns the 2d array representation of the goal board.
        """
        return self._goal_state

    def __str__(self) -> str:
        """Return a string representation of the current state.

        Returns:
            String representation of the current state.
        """
        string = ""
        for rows in self.current_state:
            for elem in rows:
                string += str(elem) + " "
        return string

    def fstring(self) -> str:
        """Return the state of this board as a formatted string.

        Returns:
            String representation of the current board containing borders.
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
        for i, row in enumerate(self.current_state):
            for j, elem in enumerate(row):
                if elem != self.goal_state[i][j]:
                    return False
        return True

    def _get_blank_spot(self) -> Tuple[int, int]:
        """Get the location of the blank space.

        Returns:
            Two-dimensional tuple containing the indices of the blank.
        """
        for i, row in enumerate(self.current_state):
            for j, elem in enumerate(row):
                if elem == "_":
                    return (i, j)
