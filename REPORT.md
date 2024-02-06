# 15-Puzzle Solver Report
### Tony Griffin
### CS 480, Spring 2024
### February 6, 2024

# Breadth First Search

## Screenshot

# Depth First Search

## Screenshot

# Informed Search
For informed search using heuristics, I designed the function to output the
number of misplaced tiles given a current board state relative to the goal
state. The list of moves utilized was the same as bread-first search; however,
their efficiencies varied drastically. This routine was highly efficient,
generating only seven nodes in total and using less than a kb in total
memory used. The time for such a routine averaged only 5 milliseconds.
The problem domain aided in this efficiency as each move throughout the
process had a different heuristic number, removing the possibility of
expanding the "wrong" node and leading to an optimal solution.

## Screenshot

