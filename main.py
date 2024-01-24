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


if __name__ == "__main__":
    main()
