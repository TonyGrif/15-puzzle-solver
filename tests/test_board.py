import numpy as np
import pytest

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
        assert board.starting_state is not None
        assert np.shape(board.starting_state) == (4, 4)

        assert np.shape(board.goal_state) == (4, 4)

    def test_move(self, board):
        pass
