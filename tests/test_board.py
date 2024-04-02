from copy import deepcopy

import pytest

from src.board import Board, GOAL_STATE
from src.utils import convert_string_to_list


@pytest.fixture
def board():
    string = "1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15"
    return Board(convert_string_to_list(string))


class TestBoard:
    def test_board_init(self, board):
        assert board.current_state is not None
        assert len(board.current_state) == 4
        assert len([row[1] for row in board.current_state]) == 4

        assert len(GOAL_STATE) == 4
        assert len([row[1] for row in GOAL_STATE]) == 4

        current = tuple(tuple(row) for row in board.current_state)
        goal = tuple(tuple(row) for row in GOAL_STATE)

        assert current != goal

    def test_strings(self, board):
        string = str(board)

        for row in board.current_state:
            for elem in row:
                assert elem in string

    def test_move(self, board):
        copy_board = deepcopy(board)
        assert board.move("Down") is False

        assert board.move("Left") is True
        current = tuple(tuple(row) for row in board.current_state)
        goal = tuple(tuple(row) for row in GOAL_STATE)
        assert current != goal

        assert board.current_state[0] == ["_", "1", "2", "4"]
        assert board.get_valid_moves() == ("Up", "Right")

        assert copy_board.move("Up") is True

        current = tuple(tuple(row) for row in board.current_state)
        copy = tuple(tuple(row) for row in copy_board.current_state)
        assert current != copy

        assert copy_board.current_state[0] == ["1", "7", "2", "4"]
        assert copy_board.current_state[1] == ["5", "_", "3", "8"]

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
        moves = ["Right", "Down", "Up", "Left", "Up", "Up", "Right", "Right"]

        for move in moves:
            board.move(move)

        assert board.is_goal_state()
