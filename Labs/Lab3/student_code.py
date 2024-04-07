import common

def minmax_tictactoe(board, turn):
	#put your code here:
	if len([i for i in board if i == common.constants.NONE]) == 0:
		return common.game_status(board)
	if turn == common.constants.X:
		result = max_value(board, turn)
		if result == -1:
			result = common.constants.O
		return result
	else:
		result = min_value(board, turn)
		return result
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return common.constants.NONE

def max_value(state, turn):
	v = -10
	status = utility(state, turn)
	if len([i for i in state if i == common.constants.NONE]) == 0 or status in [-1, 1]:
		return status
	successor_list = get_successors(state, common.constants.X)
	for i in successor_list:
		v = max(v, min_value(i, turn))
	return v

def min_value(state, turn):
	v = 10
	status = utility(state, turn)
	if len([i for i in state if i == common.constants.NONE]) == 0 or status in [-1, 1]:
		return status
	successor_list = get_successors(state, common.constants.O)
	for i in successor_list:
		v = min(v, max_value(i, turn))
	return v

def abprun_tictactoe(board, turn):
	#put your code here:
	alpha = -1
	beta = 1
	if len([i for i in board if i == common.constants.NONE]) == 0:
		return common.game_status(board)
	if turn == common.constants.X:
		result = abmax_value(board, turn, alpha, beta)
		if result == -1:
			result = common.constants.O
		return result
	else:
		result = abmin_value(board, turn)
		return result
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return common.constants.NONE

def abmax_value(state, turn, alpha, beta):
	v = -10
	status = utility(state, turn)
	if len([i for i in state if i == common.constants.NONE]) == 0 or status in [-1, 1]:
		return status
	successor_list = get_successors(state, common.constants.X)
	for i in successor_list:
		v = max(v, abmin_value(i, turn, alpha, beta))
		if v>=beta:
			return v
		alpha = max(alpha, v)
	return v

def abmin_value(state, turn, alpha, beta):
	v = 10
	status = utility(state, turn)
	if len([i for i in state if i == common.constants.NONE]) == 0 or status in [-1, 1]:
		return status
	successor_list = get_successors(state, common.constants.O)
	for i in successor_list:
		v = min(v, abmax_value(i, turn, alpha, beta))
		if v<=alpha:
			return v
		beta = min(beta, v)
	return v

def utility (board, turn):
	game_stat = common.game_status(board)
	if game_stat == 0 :
		return 0
	if game_stat == turn:
		return 1
	return -1

def get_successors(state, turn):
	successors = []
	sub_board = list(state)
	for i in range(len(state)):
		if state[i] == common.constants.NONE:
			sub_board[i] = turn
			successors.append(sub_board)
			sub_board = list(state)
	return successors
