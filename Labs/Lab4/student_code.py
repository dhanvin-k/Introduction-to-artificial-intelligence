import common

class variables:
	counter=0

def sudoku_backtracking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds
	# explored is optional but recommended
	variables.counter=0
	result = backtracking(sudoku)
	return variables.counter

def backtracking(sudoku):
	pos = currentpos(sudoku)
	if pos == 0:
		return 1
	for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
		variables.counter = variables.counter + 1
		if constraints(value, pos, sudoku):
			sudoku[pos[0]][pos[1]] = value
			result = backtracking(sudoku)
			if result != 0:
				return result
			sudoku[pos[0]][pos[1]] = 0
	return 0

def constraints(val, p, sudoku):
	y = p[0]
	x = p[1]
	row_constraint = sudoku[y]
	column_constraint = []
	for i in range(9):
		column_constraint.append(sudoku[i][x])
	if val in row_constraint:
		return 0
	elif val in column_constraint:
		return 0
	elif y in [0, 1, 2] and x in [0, 1, 2]:	# box (1,1)
		ybox = [0, 1, 2]
		xbox = [0, 1, 2]
	elif y in [3, 4, 5] and x in [0, 1, 2]: # box (2,1)
		ybox = [3, 4, 5]
		xbox = [0, 1, 2]
	elif y in [6, 7, 8] and x in [0, 1, 2]:	# box (3,1)
		ybox = [6, 7, 8]
		xbox = [0, 1, 2]
	elif y in [0, 1, 2] and x in [3, 4, 5]: # box (1,2)
		ybox = [0, 1, 2]
		xbox = [3, 4, 5]
	elif y in [3, 4, 5] and x in [3, 4, 5]: # box (2,2)
		ybox = [3, 4, 5]
		xbox = [3, 4, 5]
	elif y in [6, 7, 8] and x in [3, 4, 5]: # box (3,2)
		ybox = [6, 7, 8]
		xbox = [3, 4, 5]
	elif y in [0, 1, 2] and x in [6, 7, 8]: # box (1,3)
		ybox = [0, 1, 2]
		xbox = [6, 7, 8]
	elif y in [3, 4, 5] and x in [6, 7, 8]: # box (2,3)
		ybox = [3, 4, 5]
		xbox = [6, 7, 8]
	elif y in [6, 7, 8] and x in [6, 7, 8]: # box (3,3)
		ybox = [6, 7, 8]
		xbox = [6, 7, 8]
	for i in ybox:
		for j in xbox:
			if val == sudoku[i][j]:
				return 0
	return 1

def currentpos(sudoku):
	for i in range(len(sudoku)):
		for j in range(len(sudoku)):
			if sudoku[i][j] == 0:
				return (i, j)
	return 0

def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds
	# explored is optional but recommended
	variables.counter=0
	forwardchecking(sudoku)
	return variables.counter

def forwardchecking(sudoku):
	pos = currentpos(sudoku)
	if pos == 0:
		return 1
	domain = get_domain(sudoku, pos)
	for value in domain:
		variables.counter = variables.counter + 1
		if constraints(value, pos, sudoku):
			sudoku[pos[0]][pos[1]] = value
			result = forwardchecking(sudoku)
			if result != 0:
				return result
			sudoku[pos[0]][pos[1]] = 0
	return 0

def get_domain(sudoku, p):
	row = p[0]
	column = p[1]
	domain = []
	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
		if constraints(i, p, sudoku):
			domain.append(i)
	return domain

def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds
	# explored is optional but recommended
	variables.counter=0
	mrv(sudoku)
	return variables.counter

def mrv(sudoku):
	pos = mrv_pos(sudoku)
	if pos == 0:
		return 1
	domain = get_domain(sudoku, pos)
	for value in domain:
		variables.counter = variables.counter + 1
		if constraints(value, pos, sudoku):
			sudoku[pos[0]][pos[1]] = value
			result = mrv(sudoku)
			if result != 0:
				return result
			sudoku[pos[0]][pos[1]] = 0
	return 0

def mrv_pos(sudoku):
	count = 0
	temp = 100
	pos = 0
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				count = len(get_domain(sudoku, (i,j)))
				if count < temp:
					temp = count
					pos = (i, j)
	return pos
