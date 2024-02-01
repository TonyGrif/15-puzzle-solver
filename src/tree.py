"""This module contains the Tree and Node classes.
"""

from copy import deepcopy

import numpy as np

from src.board import Board


class Tree:
    """
    TBW
    """

    def __init__(self) -> None:
        """
        TBW
        """
        # Init with root node
        # Ensure not goal state

        # Init state tracker to set
        # Should not create new nodes of
        # prev visited state
        # Init with the root node's state

        # Init frontier with root node moves
        # Stack for dfs
        # Queue for bfs

        pass

    def expand(self) -> None:
        """
        TBW
        """
        # Ensure not at goal state
        # Get valid moves on a frontier node
        # If there is no frontier, FAIL
        # Generate new nodes for each move
        # Add to frontier
        # Add to its parent node as child
        # If node is goal state, SUCCESS
        pass

    def add_to_frontier(self) -> None:
        """
        TBW
        """
        # If frontier is stack, add to top of stack
        # If frontier is queue, add to back of queue
        # Add to frontier if the state has not already been seen or added
        # Create new node and add
        pass


class Node:
    """
    This class contains information to creating and manipluating
    nodes of a tree.

    Variables:
        parent_node (Node): The parent node for this node.
        current_board (Board): The state this node holds.
        action_used (str): The action used on the parent to reach this state.
        depth_count (int): The amount of moves that have led to this node.
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

        if isinstance(input_state, Board):
            self.current_board = input_state
        elif isinstance(input_state, Node):
            self.parent_node = input_state
            self.current_board = deepcopy(input_state.current_board)
            self.depth_count = input_state.depth_count

        if action is not None:
            self.apply_action(action)

        # Depth: increment the parent's depth val by one
        # Root count should be 0

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
        # IF GOAL STATE...

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
