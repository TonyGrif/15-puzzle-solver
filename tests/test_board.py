import numpy as np
import pytest
from copy import deepcopy

from src.board import Board
from src.utils import convert_string_to_list


@pytest.fixture
def matrix_list():
    string = "1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15"
    return convert_string_to_list(string)


@pytest.fixture
def board(matrix_list):
    return Board(matrix_list)


class TestBoard:
    def test_board_init(self, board):
        assert board.current_state is not None
        assert np.shape(board.current_state) == (4, 4)

        assert np.shape(board.goal_state) == (4, 4)

        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_array_equal,
            board.current_state,
            board.goal_state,
        )

    def test_move(self, board):
        copy_board = deepcopy(board)
        assert board.move("Down") is False

        assert board.move("Left") is True
        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_array_equal,
            board.current_state,
            board.goal_state,
        )
        assert board.current_state.tolist()[0] == ["_", "1", "2", "4"]
        assert board.get_valid_moves() == ("Up", "Right")

        assert copy_board.move("Up") is True
        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_array_equal,
            board.current_state,
            copy_board.current_state,
        )
        assert copy_board.current_state.tolist()[0] == ["1", "7", "2", "4"]
        assert copy_board.current_state.tolist()[1] == ["5", "_", "3", "8"]

    def test_get_valid_moves(self, board):
        assert board.get_valid_moves() == ("Up", "Left", "Right")

        all_list = convert_string_to_list("1 2 4 5 7 3 _ 8 9 6 11 12 13 10 14 15")
        all_board = Board(all_list)
        assert all_board.get_valid_moves() == ("Up", "Down", "Left", "Right")

        mlist = convert_string_to_list("1 2 4 5 7 3 8 9 6 11 12 13 10 14 15 _")
        corner_board = Board(mlist)
        assert corner_board.get_valid_moves() == ("Down", "Left")

    def test_is_goal_state(self, board):
        assert not board.is_goal_state()

        board.move("Right")
        board.move("Down")
        board.move("Up")
        board.move("Left")
        board.move("Up")
        board.move("Up")
        board.move("Right")
        board.move("Right")

        assert board.is_goal_state()
