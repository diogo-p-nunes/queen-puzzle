# Summary

# Algorithm Applied
  Depth First Tree Search (DFS)
 
# Problem Formulation
  Last time we added a search feature that would only take into consideration, of all the valid positions to place a queen,
  the valid positions at the leftmost free column - this because by studying the problem itself we can easily figure that
  there can only be ONE queen on each column (and line, and diagonal). With this we drastically reduced the number of
  generated nodes and the time execution, but it wasn't enough.
  
  This time, we still consider the exact same valid positions of the leftmost free column, but instead of feeding them to the
  algorithm by order (this is, from top to bottom), we feed them by a random order.
  This will allow the algorithm to venture through states first that otherwise would have been the very last (or vice-versa)
  and might find a solution way faster than before.
  
  Considering that before, the closest solution was at the very end of the state tree (worst case scenario), this time around,
  it can only get better, this is, at the very least, it will do as well as before.
  
  Function added (in the Problem subclass):
  
          def actions(self, state):
            x = board_find_free_positions_leftmostCol(state.board)
            random.shuffle(x)
            return x
 
# Conclusions
  As one can conclude from the various screenshots in results/, although the generated nodes number might vary (considerably),
  knowing that it can't get any worse than before, the results are impecable.
  We are now able to find a solution for the 50 and 100 Queens Puzzle with almost zero fuss, both (in the best case), generating
  way fewer nodes than the previous 16 Queens Puzzle.
 
 # Final Note
   With this last increment to the implemented code, I have reached my initial goal: to prove that the problem formulation
   can and will take great effect on the performance of the search algorithm (be it blind or informed).
   This was a simple project that required more sharp attention to the flow of the puzzle itself than anything else,
   exactly to prove that it is always better to first study and formulate the problem, and then start thinking about implementation.
