import sys
import os
from utils import*

''' Default values '''

nr_queens = 4
approach = 'a'
pres_sol = False

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		''' read flags '''
		for index, e in enumerate(sys.argv):
			if(e == '-a'):
				approach = verifyFlag('-a', sys.argv[index+1])
			elif(e == '-s'):
				pres_sol = True
			elif(e == '-n'):
				nr_queens = verifyFlag('-n', int(sys.argv[index+1]))
			elif(e == '--help' or e == '-h'):
				displayHelpMenu()
				sys.exit()

	if(not verifyValues(nr_queens, approach, pres_sol)):
		print('Incoherent values (--help or -h for help menu)')
		displayHelpMenu()
		sys.exit()
	
	printWelcomeMessage()
	printValues(nr_queens, approach, pres_sol)

	runComparator(nr_queens, approach, pres_sol)
	