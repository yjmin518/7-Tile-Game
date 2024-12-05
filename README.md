**A\* Search on the 7(8)-Tile Puzzle**
  
**Overview**  
This project implements the A* search algorithm to solve a variant of the classic 8-tile puzzle. The puzzle is played on a 3x3 grid with 7 numbered tiles and two empty spaces. The objective is to rearrange the tiles into numerical order, with the empty spaces at the bottom-right corner.

**Features**  
Successor Generation: Calculates and displays all valid successor states from a given configuration, sorted in ascending order based on the state representation.
A Search Solution*:
- Finds the optimal path from a given starting state to the goal state.
- Uses the Manhattan distance as the heuristic function.
- Tracks and prints the path, heuristic values, number of moves, and maximum queue length.

**Usage**
The project includes two main functions:  
- print_succ(state): Prints all successor states and their heuristic values for a given input state.
- solve(state): Solves the puzzle using the A* algorithm and prints the solution path and statistics.

This project was created as part of an assignment for CS540 @ UW Madison.
