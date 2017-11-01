import copy
import sys
from random import shuffle
from search import *
from utils import *

approach = 'a'
pres_sol = False

def create_board(nr_queens):
	board = []
	line = []

	for i in range(nr_queens):
		for j in range(nr_queens):
			line.append('.')
		board.append(line)
		line = []

	return board

def get_pos_value(pos, board):
	return board[pos[0]][pos[1]]

def line_attacked(line, board):
	length = len(board[line])
	for i in range(length):
		if(board[line][i] == '.'):
			board[line][i] = 'X'

def col_attacked(col, board):
	length = len(board)
	for i in range(length):
		if(board[i][col] == '.'):
			board[i][col] = 'X'

def right_diag_attacked(line, col, board):
	lineMin = 0
	lineMax = len(board)
	colMin = 0
	colMax = lineMax

	lineInit = line
	colInit = col

	#Top most diagonal
	while(line >= lineMin and col >= colMin):
		if (board[line][col] == '.'):
			board[line][col] = 'X'
		line -= 1
		col -= 1

	line = lineInit
	col = colInit

	#Bottom most diagonal
	while(line < lineMax and col < colMax):
		if (board[line][col] == '.'):
			board[line][col] = 'X'
		line += 1
		col += 1

def left_diag_attacked(line, col, board):
	lineMin = 0
	lineMax = len(board)
	colMin = 0
	colMax = lineMax

	lineInit = line
	colInit = col

	#Top most diagonal
	while(line >= lineMin and col < colMax):
		if (board[line][col] == '.'):
			board[line][col] = 'X'
		line -= 1
		col += 1

	line = lineInit
	col = colInit

	#Bottom most diagonal
	while(line < lineMax and col >= colMin):
		if (board[line][col] == '.'):
			board[line][col] = 'X'
		line += 1
		col -= 1

def set_attacked(pos, board):
	line_attacked(pos[0], board)
	col_attacked(pos[1], board)
	right_diag_attacked(pos[0], pos[1], board)
	left_diag_attacked(pos[0], pos[1], board)


def place_queen(pos, board):
	board_mimic = copy.deepcopy(board)
	board_mimic[pos[0]][pos[1]] = 'Q'	
	set_attacked(pos, board_mimic)
	return board_mimic

def board_find_free_positions(board):
	l = []
	length = len(board)
	for i in range(length):
		for j in range(length):
			pos = (i,j)
			if(get_pos_value( pos, board ) == '.'):
				l.append(pos)
	return l

def board_nr_queens_and_invalid_pos(board):
	counter_queens = 0
	counter_invalid = 0
	length = len(board)
	for i in range(length):
		for j in range(length):
			pos = (i,j)
			value = get_pos_value( pos, board )
			if(value == 'Q'):
				counter_queens += 1
			elif(value == 'X'):
				counter_invalid += 1
	return (counter_queens, counter_invalid)

def board_find_free_positions_leftmostCol(board):
	l = []
	length = len(board)
	for j in range(length):
		for i in range(length):
			pos = (i,j)
			if(get_pos_value( pos, board ) == '.'):
				l.append(pos)
		if(l):
			break
	return l



class queen_chess_state(object):
	def __init__(self, board):
		self.board = board
		self.queens , self.invalid_pos = board_nr_queens_and_invalid_pos(board)

	def __str__(self):
		return str(self.board)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.board == other.board
		else:
			return False

	def __lt__(self, other):
		return self.queens < other.queens

	def __hash__(self):
		return id(self)

class queen_chess(Problem):

	def __init__(self, nr_queens):
		board = create_board(nr_queens)
		state = queen_chess_state(board)
		goal = nr_queens
		self.pres_sol = pres_sol
		self.board = board
		super(queen_chess, self).__init__(state, goal)

	def actions(self, state):
		if(approach == 'r'):
			x = board_find_free_positions_leftmostCol(state.board)
			shuffle(x)
			return x
		if(approach == 'l'):
			return board_find_free_positions_leftmostCol(state.board)
		else:
			return board_find_free_positions(state.board)

	def result(self, state, action):
		return queen_chess_state(place_queen(action, state.board))

	def get_goal(self):
		return self.goal
	

def compare_searchers2(problems, header,
                      searchers=[depth_first_tree_search
                                 ]):
    def do(searcher, problem):
        p = InstrumentedProblem(problem)
        searcher(p)
        return p

    table = [[name(s)] + [do(s, p) for p in problems] for s in searchers]
    print_table(table, header)
    print()


def compare_graph_searchers2(nr_queens):
    """Prints a table of search results."""
    compare_searchers2(problems=[queen_chess(nr_queens)
                                ],
                      header=['Searcher', 'Tab-1',
                              'Tab-2', 'Tab-3', 'Tab-4', 'Tab-5'])
		


if(len(sys.argv) < 2):
	print('number of queens not specified. Please write:\n [time] python3.5 queen-puzzle.py NUMBER-OF-QUEENS')
	sys.exit()
else:
	
	approach = sys.argv[2]
	if(sys.argv[3] == 'False'):
		pres_sol = False
	else:
		pres_sol = True
	compare_graph_searchers2(int(sys.argv[1]))