"""This module contains the Tree and Node classes.
"""

import logging
from collections import deque
from copy import deepcopy
from typing import Tuple

import numpy as np

from src.board import Board


class Node:
    """This class contains information to creating and manipluating
    nodes of a tree.

    Variables:
        parent_node (Node): The parent node for this node.
        current_board (Board): The state this node holds.
        action_used (str): The action used on the parent to reach this state.
        depth_count (int): The amount of moves that have led to this node.
        children (List[Node]): A list of nodes created from this node.
    """

    def __init__(self, state: Board, action: str = None, parent: "Node" = None) -> None:
        """Default constructor for a Node object. This is intended to be used
        for the creation of root nodes; all children nodes should ideally be
        created through public methods.

        Parameters:
            input_state (Board or Node): The state this node will hold.
            action (str): The valid move of this object. This move will
                be applied to a deep copy of the state's current
                board and stored in this nodes current board.
            parent (Node): The parent node for this Node.
        """
        self._parent_node = None if parent is None else parent
        self._current_board = deepcopy(state)

        self._action_used = action
        self.depth_count = 0 if parent is None else parent.depth_count
        self._apply_action(action)

        self.children = []

    @property
    def parent_node(self) -> "Node":
        """Return the parent Node of this Node if one exists.

        Returns:
            Returns the parent Node if there is one; None otherwise.
        """
        return self._parent_node

    @property
    def current_board(self) -> Board:
        """Return the Board state this Node holds.

        Returns:
            The Board object this Node tracks.
        """
        return self._current_board

    @property
    def action_used(self) -> str:
        """Return the string representation of the move used to achieve
        the current state from the parent.

        Returns:
            String representation of a move.
        """
        return self._action_used

    def get_parent_array(self) -> np.ndarray:
        """Return the parent state of this array.

        Returns:
            The parent state in the form of a numpy array.
        """
        return self.parent_node.current_board.current_state

    def get_current_array(self) -> np.ndarray:
        """Return the current state of this array.

        Returns:
            The current state in the form of a numpy array.
        """
        return self.current_board.current_state

    def get_current_string(self) -> str:
        """Return the string state of this Node.

        Returns:
            String representation of this Node.
        """
        return str(self.current_board)

    def get_moves(self) -> Tuple[str]:
        """Wrapper function to get the moves of this node based on state.

        Returns:
            A tuple of string moves.
        """
        return self.current_board.get_valid_moves()

    def move_board(self, action: str) -> "Node":
        """Make a new Node by moving the current state.

        Parameters:
            action (str): The valid action to apply.

        Returns:
            A newly created node.
        """
        new_node = Node(self.current_board, action, self)
        self.children.append(new_node)
        return new_node

    def _apply_action(self, action: str) -> None:
        """Apply a valid move to the current state of this node. Invalid
        moves will be discarded. This function also presumes this
        node's current_state variable is a deep copy.

        Parameters:
            action (str): The valid action to apply.
        """
        if self.current_board.move(action) is not False:
            self._increment_depth()

    def _increment_depth(self) -> None:
        """Increment the depth counter by one upon successful action."""
        self.depth_count += 1

    def is_goal_state(self) -> bool:
        """Determine if the current board state is the goal state.

        Returns:
            True if this is the goal state, False otherwise.
        """
        return self.current_board.is_goal_state()


class Tree:
    """This class contains information to creating and manipulating
    a search tree.

    Variables:
        root (Node): The root node for this Tree.
        expand_count (int): The number of nodes this tree has expanded.
        explored_set (List[str]): The collection of states that have already been
            seen by this tree.
        frontier (deque[Node]): The collection of all unexpanded nodes.
    """

    def __init__(self, root: Node) -> None:
        """Default constructor for a Tree object.

        Parameters:
            root (Node): The root node of this tree.
        """
        self.root = None
        self.expand_count = 0
        self.explored_set = set()
        self._frontier = deque()

        if root.is_goal_state():
            raise AssertionError("Root is already in goal state.")

        self.root = root
        self._frontier.append(self.root)
        logging.info("Creating new tree with %s", root.get_current_array().tolist())

    def expand(self) -> Node:
        """Expand the current node to create new nodes based on valid moves.
        The node selected will be pulled from the frontier.

        Throws:
            IndexError if the frontier is empty.

        Returns:
            Return the Node if a goal state has been reached; None otherwise.
        """
        if self.get_length_of_frontier() == 0:
            raise IndexError("No solution found.")
        node = self._frontier.popleft()

        if node.is_goal_state() is True:
            logging.info("Goal state found %s", node.get_current_string())
            return node

        if self._add_to_set(node) is True:
            logging.info(
                "Expanding node %s with depth %s",
                node.get_current_array().tolist(),
                node.depth_count,
            )
            self._add_moves_to_frontier(node)

        self._increment_expand_counter()
        return None

    def get_length_of_frontier(self) -> int:
        """Get the length of the current frontier.

        Returns:
            Integer length of the frontier.
        """
        return len(self._frontier)

    def _add_moves_to_frontier(self, node: Node) -> None:
        """Add new unexplored nodes to the frontier.

        Parameters:
            node (Node): The node to expand.
        """
        for moves in node.get_moves():
            new_node = Node(node.current_board, moves, node)
            self._frontier.append(new_node)
            logging.debug(
                "New node added to frontier: %s", new_node.get_current_array().tolist()
            )

    def _add_to_set(self, state: Node) -> bool:
        """Add the node's state to the set if it has not already been seen.

        Parameters:
            state (Node): The node containing a state.

        Returns:
            True if the state was sucessfully added, False otherwise.
        """
        if state.get_current_string() in self.explored_set:
            return False

        self.explored_set.add(state.get_current_string())
        return True

    def _increment_expand_counter(self) -> None:
        """Increment the number of expanded nodes by one."""
        self.expand_count += 1
