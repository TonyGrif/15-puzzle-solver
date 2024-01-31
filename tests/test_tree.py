import pytest

from src.utils import convert_string_to_list
from src.board import Board
from src.tree import Tree, Node


@pytest.fixture
def root_node():
    string = "1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15"
    board = Board(convert_string_to_list(string))
    return Node(board)


@pytest.fixture
def tree():
    return None


class TestNode:
    def test_init(self, root_node):
        assert root_node.parent_state is None
        assert root_node.current_state is not None

        child_node = Node(root_node)
        assert child_node.parent_state is not None
        assert child_node.current_state is not None
        assert root_node.current_state == child_node.parent_state


class TestTree:
    def test_import(self):
        assert True
