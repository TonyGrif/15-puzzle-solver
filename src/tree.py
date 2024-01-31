"""This module contains the Tree and Node classes.
"""

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
    TBW
    """

    def __init__(self) -> None:
        """
        TBW
        """
        # Init with action ("Up", "Down"...)
        # Init with parent node (not a deep copy)
            # Like a linked list
            # Root will be none

        # Deep copy parent node board to self node var
        # Perform move on deep copy board and store in state

        # Path-cost will always be one (no need to implement)
        # Depth: increment the parent's depth val by one
            # Root count should be 0
        pass

    def apply_action(self) -> None:
        """
        TBW
        """
        # Perform the move operation on the deep copy parent current state
        # Return new current state
        # IF GOAL STATE...
        pass

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
