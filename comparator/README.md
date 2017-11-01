# _____________Help Menu_____________

# Description:

    This tool let's you compare the results for the different types of approches
    one can take to formulate the same problem.
    The results include the time of execution and a table with the following values, in order:

    _search algorithm_   <Generated nodes  /  Nr of goal testes  /  Expanded nodes>

# Available Flags:

   -n _N_: number of queens to puzzle with
           (N > 3)
           For brute-force - N < 13
           For leftmost-column - N < 31

   -a _type_: type = b (brute-force)
              type = l (leftmost-colmun)
              type = r (rand(leftmost-column))
              type = a (all types)

   -s: show solution
       (might distort depending on window's size)

# Default Values:

    _N_ = 4
    _type_ = a
    _no solution_

# Running example:

    python3.5 comparator.py -n 8 -a a -s
    (flag order does not matter)
