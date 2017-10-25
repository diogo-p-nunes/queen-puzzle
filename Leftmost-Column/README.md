# Summary

# Algorithm
 Blind Search by DFS

# Problem Formulation
  
  Having studied for a while the fundamentals of the problem (puzzle) one quickly understands that the number of queens
  to place is always equal to the number of lines and columns. Knowing how the Queen attacks in chess, this means that for
  each column can only be one queen and for each line the exact same.
  This way, for every queen to be placed, the valid positions that are more interesting to try first (and the only actually
  usefull to try) are at the top of the leftmost free column. 
  This function implements exactly that and returns this list of available positions (Considerably smaller than all valid
  board positions when we scale to (n x n) boards).

      board_find_free_positions_leftmostCol(board)
      
# Conslusions

  By the result/ files, we now see that the number of generated and expanded nodes is considerably smaller and therefore 
  the execution time as well.
  This allows us to experiment with larger queen numbers.
  
# Considerations

  As far as problem formulation goes, one might say it doesn't get substantially better than this 
  (please correct me if I'm wrong)
  To achieve and solve the problem for bigger values of queen number, the next step is to step out of the dark
  and adventure into the informed (or heuristic) searchs.
