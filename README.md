# 15-puzzle-solver
Solves a 15-puzzle problem by utilizing BFS, DFS, and Informed Search using Heuristics.

## Requirements
* [Python 3.9+](https://www.python.org/)

All further requirements can be installed using [Poetry]("https://python-poetry.org/")
(poetry install).

## Running Instructions
To run the agent program, use `./agent.py [routine] [starting state]` where routine must be either `bfs`, `dfs`, or `ish`.
The starting state must be a single string containing the numbers 1-15 and a blank character in the form of `_`. If no
starting state is provided, the default state will be `"1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15"`.

To run user-game, use `./play.py [starting state]` where the starting state must take the same form as the agent script.
The user will be prompted for a move input that must be input with the same capitalization as the prompt, although the
`''` are unneeded.

## [Report](report/REPORT.md)
