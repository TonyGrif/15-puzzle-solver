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
def tree(root_node):
    return Tree(root_node)


class TestNode:
    def test_init(self, root_node):
        assert root_node.parent_node is None
        assert root_node.current_board is not None
        assert root_node.children == []

        child_node = Node(root_node)
        assert child_node.parent_node is not None
        assert child_node.parent_node is root_node

        assert child_node.children == []
        assert len(root_node.children) == 1
        assert root_node.children[0] is child_node

        assert isinstance(child_node.parent_node, Node)
        assert isinstance(child_node.current_board, Board)
        assert child_node.current_board is not None
        np.testing.assert_array_equal(
            root_node.get_current_array(), child_node.get_parent_array()
        )

        assert root_node.action_used is None
        assert root_node.depth_count == 0
        assert child_node.action_used is None
        assert child_node.depth_count == 0

    def test_action(self, root_node):
        child_node = Node(root_node, "Up")
        assert child_node.parent_node is not None
        assert child_node.current_board is not None
        assert child_node.depth_count == 1

        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_array_equal,
            child_node.get_current_array(),
            child_node.get_parent_array(),
        )

        np.testing.assert_array_equal(
            child_node.get_parent_array(), root_node.get_current_array()
        )
        assert child_node.parent_node is root_node

        assert child_node.get_current_array().tolist()[0] == ["1", "7", "2", "4"]
        assert child_node.action_used == "Up"

        grandchild_node = Node(child_node, "Left")
        assert grandchild_node.action_used == "Left"
        assert grandchild_node.depth_count == 2

        child_node = Node(root_node, "Down")
        assert child_node.action_used is None
        np.testing.assert_array_equal(
            child_node.get_current_array(), child_node.get_parent_array()
        )


class TestTree:
    def test_init(self, tree):
        assert tree.root is not None
        assert tree.expand_count == 0
        assert tree.root.get_current_string() not in tree.explored_set
        assert len(tree.frontier) == 1
        assert len(tree.explored_set) == 0

        goal_board = Board(
            convert_string_to_list("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 _")
        )
        with pytest.raises(Exception) as e:
            fail = Tree(goal_board)

    def test_expand(self, tree):
        assert len(tree.frontier) == 1

        tree.expand()
        assert len(tree.frontier) == 3
        assert tree.root.get_current_string() in tree.explored_set
        assert tree.expand_count == 1

        tree.expand()
        assert len(tree.frontier) == 6
        assert tree.expand_count == 2

    def test_add_to_set(self, tree):
        assert tree.root.get_current_string() not in tree.explored_set
        
        tree.expand()
        assert tree.root.get_current_string() in tree.explored_set
        assert len(tree.explored_set) == 1

        tree.expand()
        assert len(tree.explored_set) == 2
