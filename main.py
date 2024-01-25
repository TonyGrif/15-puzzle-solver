#!/usr/bin/env python3

"""Main module for the 15-Puzzle Solver."""

import argparse
import logging


def main():
    """Main driver of the 15-Puzzle Solver script."""
    parser = argparse.ArgumentParser(
        description="Solve a 15-Puzzle through multiple AI methods."
    )

    parser.add_argument(
        "matrix_string",
        type=str,
        default="1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15",
        nargs="?",
        help="The starting state of the program.",
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

    matrix_list = args.matrix_string.split(" ")
    logging.debug("%s: %s", type(matrix_list), matrix_list)


if __name__ == "__main__":
    main()
