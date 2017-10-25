# queen-puzzle
Where I implement, in python3.5, different search algorithms and methods to solve the Queen Puzzle (n-queens-puzzle)
Follow this Wikipedia link to learn more about this puzzle: https://en.wikipedia.org/wiki/Eight_queens_puzzle

# Description
The objective is to find new and different ways to formulate the same problem (Queen puzzle) so that the number of generated and expanded nodes can be decreased enough to solve the problem for large numbers of queens.

    # Short Implementation Explanation
      
      Given a number 'n' of queens to play with, an empty (represented by '.') board(n x n) is created, represented as a list
      of lists, each containing the various column values.
      
      When a queen is placed in a certain position, immediatly that row, column, and both diagonals are no longer valid
      positions to place the next one (marked with an 'X').
      
      The objective is to place the 'n' queens so that none is attacked by another.
      
      The various search algorithms will start with an empty board and will expand the initial state in order to find the
      objective (goal state), that is, having no more queens to place.

# Organization
Each folder contains a variation of the problem implemented and explained, as well as experimental results.

# Running
Under the assumption that the 3 files, queen-puzzle.py, search.py and utils.py are in the same directory, one only has to run the following command

    [time] python3.5 queen-puzzle.py
    
# Output
The output contains the solution found (board representation) and a table which contains:

    Searcher                      Tab-1
    Search algorithm apllied      < Nodes generated / Goal tests / Nodes expanded>

This comes of great help to compare multiple algorithms' performance.
