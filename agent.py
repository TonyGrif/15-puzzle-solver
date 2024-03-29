#!/usr/bin/env python3

"""Main module for the 15-Puzzle Solver."""

import argparse
import logging
import time

import psutil

from src.board import Board
from src.tree import Node, Tree
from src.utils import convert_string_to_list, validate_list


def main():
    """Main driver of the 15-Puzzle Solver script."""
    parser = argparse.ArgumentParser(
        description="Solve a 15-Puzzle through multiple AI methods."
    )

    parser.add_argument(
        "search_routine",
        type=str,
        choices=["bfs", "dfs", "ish"],
        help="The search algorithm to use on this puzzle.",
    )

    parser.add_argument(
        "matrix_string",
        type=str,
        default="1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15",
        nargs="?",
        help="The starting state of the program able to create a 4x4 matrix.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        dest="logging_level",
        const=logging.INFO,
        help="Output verbose info logs to console.",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_const",
        dest="logging_level",
        const=logging.DEBUG,
        help="Output all program debug logs to console.",
    )

    args = parser.parse_args()
    logging.basicConfig(level=args.logging_level)

    matrix_list = convert_string_to_list(args.matrix_string)

    try:
        validate_list(matrix_list)
    except AssertionError as ae:
        print(ae)
        return

    logging.debug("Running %s routine on %s", args.search_routine, matrix_list)
    game_board = Board(matrix_list)
    tree = Tree(Node(game_board), args.search_routine)

    start = time.perf_counter()
    start_mem = psutil.Process().memory_info().rss
    while len(tree.goal_states) == 0:
        tree.expand()
    end = time.perf_counter()
    end_mem = psutil.Process().memory_info().rss

    print(
        f"""
        Search Routine: {tree.routine}\n
        Moves: {tree.goal_states[0].action_used}\n
        Expanded Node Count: {tree.expand_count}\n
        Time Taken: {round((end - start) * 1000)} ms\n
        Memory Used: {((end_mem - start_mem) / 1000):.2f} kb\n
    """
    )


if __name__ == "__main__":
    main()
