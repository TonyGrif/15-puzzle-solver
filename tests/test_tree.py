import numpy as np
import pytest

from src.board import Board
from src.tree import Node, Tree
from src.utils import convert_string_to_list


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
        np.testing.assert_array_equal(
            root_node.get_current_array(), child_node.get_parent_array()
        )

    def test_action(self, root_node):
        child_node = Node(root_node, "Up")
        assert child_node.parent_state is not None
        assert child_node.current_state is not None

        assert child_node.parent_state != child_node.current_state
        assert child_node.parent_state == root_node.current_state
        assert child_node.get_current_array().tolist()[0] == ["1", "7", "2", "4"]
        assert child_node.action_used == "Up"

        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_array_equal,
            child_node.get_current_array(),
            child_node.get_parent_array(),
        )

        child_node = Node(root_node, "Down")
        assert child_node.action_used is None
        np.testing.assert_array_equal(
            child_node.get_current_array(), child_node.get_parent_array()
        )


class TestTree:
    def test_import(self):
        assert True
