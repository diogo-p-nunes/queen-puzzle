welcome = '\n\n#__________Implemented by Diogo Nunes__________#\n\t\t  01-11-2017\n'
values = '______values________\n'
line = '____________________'

#___________________________________
# Help Menu

title = '\n_____________Help Menu_____________\n'

description = '# Description:\n'
desc = "    This tool let\'s you compare the results for the different types of approches\n    one can take to formulate the same problem."
desc1 = "    The results include the time of execution and a table with the following values, in order:"
desc2 = '\n    _search algorithm_   <Generated nodes  /  Nr of goal testes  /  Expanded nodes>'

flags = '\n# Available Flags:\n'
n_queens = '   -n _N_: number of queens to puzzle with\n           (N > 3)\n           For brute-force - N < 13\n           For leftmost-column - N < 31\n'
approach = '   -a _type_: type = b (brute-force)\n              type = l (leftmost-colmun)\n              type = r (rand(leftmost-column))\n              type = a (all types)\n'
pres_sol = "   -s: show solution\n       (might distort depending on window\'s size)"

default = '\n# Default Values:\n'
default_val = '    _N_ = 4\n    _type_ = a\n    _no solution_'

example_title = '\n# Running example:\n'
example = '    python3.5 comparator.py -n 8 -a a -s'
explain = '    (flag order does not matter)\n'
