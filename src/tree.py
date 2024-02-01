"""This module contains the Tree and Node classes.
"""

import logging
from collections import deque
from copy import deepcopy
from typing import Tuple

import numpy as np

from src.board import Board


class Node:
    """
    This class contains information to creating and manipluating
    nodes of a tree.

    Variables:
        parent_node (Node): The parent node for this node.
        current_board (Board): The state this node holds.
        action_used (str): The action used on the parent to reach this state.
        depth_count (int): The amount of moves that have led to this node.
        children (List[Node]): A list of nodes created from this node.
    """

    def __init__(self, input_state: Board or Node, action: str = None) -> None:
        """
        Default constructor for a Node object.

        Parameters:
            input_state (Board or Node): The state this node will hold. The root node
                should be initialized using the Board; all other nodes should be
                initialized by passing in the parent node.
            action (str): The valid move of this object. This move will applied to
                a deep copy of the parent's current board and stored in this nodes
                current board.
        """
        self.parent_node = None
        self.current_board = None
        self.action_used = None
        self.depth_count = 0
        self.children = []

        if isinstance(input_state, Board):
            self.current_board = input_state
        elif isinstance(input_state, Node):
            self.parent_node = input_state
            self.current_board = deepcopy(input_state.current_board)
            self.depth_count = input_state.depth_count

            # Linking this Node to the parent
            input_state.children.append(self)

        if action is not None:
            self.apply_action(action)

    def get_parent_array(self) -> np.ndarray:
        """
        Return the parent state of this array.

        Returns:
            The parent state in the form of a numpy array.
        """
        return self.parent_node.current_board.current_state

    def get_current_array(self) -> np.ndarray:
        """
        Return the current state of this array.

        Returns:
            The current state in the form of a numpy array.
        """
        return self.current_board.current_state

    def get_current_string(self) -> str:
        """
        Return the string state of this Node.

        Returns:
            String representation of this Node.
        """
        return str(self.current_board)

    def get_moves(self) -> Tuple[str]:
        """
        Wrapper function to get the possible moves of this node based on state.

        Returns:
            A tuple of string moves.
        """
        return self.current_board.get_valid_moves()

    def apply_action(self, action: str) -> None:
        """
        Apply a valid move to the current state of this node. Invalid
        moves will be discarded. This function also presumes this
        node's current_state variable is a deep copy.

        Parameters:
            action (str): The valid action to apply.
        """
        if self.current_board.move(action) is not False:
            self.action_used = action
            self.increment_depth()

    def increment_depth(self) -> None:
        """
        Increment the depth counter by one upon successful action.
        """
        self.depth_count += 1

    def is_goal_state(self) -> bool:
        """
        Determine if the current board state is the goal state.

        Returns:
            True if this is the goal state, False otherwise.
        """
        return self.current_board.is_goal_state()


class Tree:
    """
    This class contains information to creating and manipulating
    a search tree.

    Variables:
        root (Node): The root node for this Tree.
        expand_count (int): The number of nodes this tree has expanded.
        explored_set (list): The collection of nodes that have already been
            seen by this tree.
        frontier (deque): The collection of all unexpanded nodes.
    """

    def __init__(self, root: Node) -> None:
        """
        Default constructor for a Tree object.

        Parameters:
            root (Node): The root node of this tree.
        """
        self.root = None
        self.expand_count = 0
        self.explored_set = set()
        self.frontier = deque()

        if root.is_goal_state():
            raise (AssertionError("Root is already in goal state."))

        self.root = root
        self.frontier.append(self.root)
        logging.info("Creating new tree with %s", root.get_current_array().tolist())

    def expand(self) -> Node:
        """
        Expand the current node to create new nodes based on valid moves. The
        node selected will be pulled from the frontier.

        Throws:
            IndexError if the frontier is empty.

        Returns:
            Return the Node if a goal state has been reached; None otherwise.
        """
        if len(self.frontier) == 0:
            raise (IndexError("No solution found."))
        node = self.frontier.popleft()

        if node.is_goal_state() is True:
            logging.info("Goal state found %s", node.get_current_string())
            return node

        if self.add_to_set(node) is True:
            logging.info(
                "Expanding node %s with depth %s",
                node.get_current_array().tolist(),
                node.depth_count,
            )
            self.add_moves_to_frontier(node)

        self.increment_expand_counter()
        return None

    def add_moves_to_frontier(self, node: Node) -> None:
        """
        Add new unexplored nodes to the frontier.

        Parameters:
            node (Node): The node to expand.
        """
        for moves in node.get_moves():
            new_node = Node(node, moves)
            self.frontier.append(new_node)
            logging.debug(
                "New node added to frontier: %s", new_node.get_current_array().tolist()
            )

    def add_to_set(self, state: Node) -> bool:
        """
        Add the node's state to the set if it has not already been seen.

        Parameters:
            state (Node): The node containing a state.

        Returns:
            True if the state was sucessfully added, False otherwise.
        """
        if state.get_current_string() in self.explored_set:
            return False

        self.explored_set.add(state.get_current_string())
        return True

    def increment_expand_counter(self) -> None:
        """
        Increment the number of expanded nodes by one.
        """
        self.expand_count += 1
