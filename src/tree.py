"""This module contains the Tree and Node classes.
"""

from copy import deepcopy
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
        parent_state (Board): The parent state this node holds.
        current_state (Board): The state this node holds.
    """

    def __init__(self, input_state: Board or Node, action: str = None) -> None:
        """
        Default constructor for a Node object.

        Parameters:
            input_state (Board or Node): The state this node will hold. The root node
                should be initialized using the Board; all other nodes should be
                initialized by passing in the parent node.
            action (str): The valid move jof this object. This move will applied to
                a deep copy of the parent's current board and stored in this nodes
                current board.
        """
        self.parent_state = None
        self.current_state = None
        self.action_used = None

        if type(input_state) is Board:
            self.current_state = input_state
        elif type(input_state) is Node:
            self.parent_state = input_state.current_state
            self.current_state = deepcopy(input_state.current_state)

        if action is not None:
            self.apply_action(action)

        # Path-cost will always be one (no need to implement)
        # Depth: increment the parent's depth val by one
        # Root count should be 0
        pass

    def apply_action(self, action: str) -> None:
        """
        Apply a valid move to the current state of this node. Invalid
        moves will be discarded. This function also presumes this
        node's current_state variable is a deep copy.

        Parameters:
            action (str): The valid action to apply.
        """
        if self.current_state.move(action) is not None:
            self.action_used = action
        # IF GOAL STATE...

    def increment_depth(self) -> None:
        """
        TBW
        """
        # If parent is root, set to 1
        # If this node is root, set to 0
        # Otherwise, increment depth by one
        pass

    def is_goal_state(self) -> None:
        """
        TBW
        """
        # Wrapper around board's is_goal_state function
        # Return the moves used if so
        pass
