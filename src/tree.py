"""This module contains the Tree and Node classes.
"""

import logging
from queue import LifoQueue, SimpleQueue
from copy import deepcopy
from typing import Deque, List, Set, Tuple

import numpy as np

from src.board import Board


class Node:
    """This class contains information to creating and manipluating
    nodes of a tree.

    Variables:
        parent_node (Node): The parent node for this node.
        current_board (Board): The state this node holds.
        action_used (list[str]): The actions used on the parent to reach this state.
        depth_count (int): The amount of moves that have led to this node.
        children (List[Node]): A list of nodes created from this node.
    """

    def __init__(self, state: Board, action: str = None, parent: "Node" = None) -> None:
        """Default constructor for a Node object. This is intended to be used
        for the creation of root nodes; all children nodes should ideally be
        created through public methods.

        Parameters:
            input_state (Board): The state this node will hold.
            action (str): The valid move of this object. This move will
                be applied to a deep copy of the state's current
                board and stored in this nodes current board.
            parent (Node): The parent node for this Node.
        """
        self._parent_node = None if parent is None else parent
        self._current_board = deepcopy(state)

        self._action_used = [] if parent is None else deepcopy(parent.action_used)
        if action is not None:
            self.action_used.append(action)
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
    def action_used(self) -> List[str]:
        """Return the string representation of the move used to achieve
        the current state from the parent.

        Returns:
            List of string representations of a move.
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
        goal_states(List[Node]): The list of goal state nodes found.
        routine (str): The routine used for this search tree.
    """

    def __init__(self, root: Node, routine: str) -> None:
        """Default constructor for a Tree object.

        Parameters:
            root (Node): The root node of this tree.
            routine (str): The routine used for this search tree.
        """
        self._root = root
        self.expand_count = 0
        self._explored_set = set()
        self._goal_states = []

        if routine not in ("bfs", "dfs"):
            raise AssertionError("Routine requested has not been implemented")

        self._routine = routine
        if routine == "bfs":
            self._frontier = SimpleQueue()
        elif routine == "dfs":
            self._frontier = LifoQueue()

        if root.is_goal_state():
            raise AssertionError("Root is already in goal state.")

        self._frontier.put(self.root)
        logging.info("Creating new tree with %s", root.get_current_array().tolist())

    @property
    def root(self) -> Node:
        """Return the root of this Tree.

        Returns:
            Node representation of the root of this Tree.
        """
        return self._root

    @property
    def explored_set(self) -> Set[str]:
        """Return the explored set of this Tree.

        Returns:
            Set of strings containing the states seen by this Tree.
        """
        return self._explored_set

    @property
    def frontier(self) -> Deque[Node]:
        """Return the current frontier of this Tree.

        Returns:
            Deque of Nodes not expanded.
        """
        return self._frontier

    @property
    def goal_states(self) -> List[Node]:
        """Return the collection of goal states this tree has.

        Returns:
            List of Nodes that are in goal state.
        """
        return self._goal_states

    @property
    def routine(self) -> str:
        """Return the search routine used.

        Returns:
            String representation of the routine used.
        """
        return self._routine

    def expand(self) -> None:
        """Expand the current node to create new nodes based on valid moves.
        The node selected will be pulled from the frontier.

        Throws:
            IndexError if the frontier is empty.

        Returns:
            Return the Node if a goal state has been reached; None otherwise.
        """
        if self.frontier.qsize() == 0:
            raise IndexError("No solution found.")

        node = None
        node = self.frontier.get()

        if node.is_goal_state() is True:
            logging.info("New goal state found.")
            self.goal_states.append(node)
            return

        if self._add_to_set(node) is True and node.depth_count <= 16:
            self._add_moves_to_frontier(node)

        self._increment_expand_counter()

    def _add_moves_to_frontier(self, node: Node) -> None:
        """Add new unexplored nodes to the frontier.

        Parameters:
            node (Node): The node to expand.
        """
        for moves in node.get_moves():
            new_node = node.move_board(moves)
            self._frontier.put(new_node)
            logging.debug("New node added to frontier with depth %s", node.depth_count)

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
