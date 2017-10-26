# Summary

# Algorithm
  Blind Search by DFS

# Problem Formulation 
  This is the simplest it can ever get.
  Since every position marked with 'X' is invalid to place a queen, I simply implemented a function that runs
  through the board (top to bottom, left to right) and returns a list of all the available positions.

        board_find_free_positions(board)
 
# Conclusions
  By the result/ files, one can confirm that a blind search (DFS), given all the possible valid positions at once, will
  very rapidly turn into a gigantic state tree.
  The exponentiality of its time complexity is highlighted when the problem is with 12 queens instead of the classic 
  8 queens puzzle.
  By the number of generated and expanded nodes, one might also note the exponentiality of space complexity of such
  algorithm and problem formulation.
  
  Not at all the best algorithm and problem formulation.
