import common

def part_one_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	w = []
	for i in range(common.constants.NUM_FEATURES):
		w.append(0)
	converge = False
	while not converge:
		converge = True
		for i in range(common.constants.TRAINING_SIZE):
			classify = w[0]*data_train[i][0] + w[1]*data_train[i][1]  + w[2]
			if classify>=0:
				classify = 1
			else:
				classify = 0
			if classify == data_train[i][2]:
				pass
			else:
				converge = False
				if classify==0:
					w[0] = w[0] + data_train[i][0]
					w[1] = w[1] + data_train[i][1]
					w[2] = w[2] + 1
				else:
					w[0] = w[0] - data_train[i][0]
					w[1] = w[1] - data_train[i][1]
					w[2] = w[2] - 1
	for i in range(common.constants.TEST_SIZE):
		temp = w[0]*data_test[i][0] + w[1]*data_test[i][1] + w[2]
		if temp>=0:
			data_test[i][2] = 1
		else:
			data_test[i][2] = 0
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in
	# index 0 and Y in index 1, and a blank space in index 2
	# to be filled with class
	# The class value could be a 0 or a 1
	return

def part_two_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	w = []
	classify = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for y in range(common.constants.NUM_CLASSES):
		w.append([])
		for x in range(common.constants.NUM_FEATURES):
			w[y].append(0)
	converge = False
	count = len(data_train)
	margin =  0.05
	multiplier = 0.25
	while count > float(len(data_train)) * margin:
		count = 0
		for i in range(common.constants.TRAINING_SIZE):
			for j in range(common.constants.NUM_CLASSES):
				classify[j] = w[j][0]*data_train[i][0] + w[j][1]*data_train[i][1]  + w[j][2]
			pos = classify.index(max(classify))
			if pos == data_train[i][2]:
				pass
			else:
				count += 1
				w[int(data_train[i][2])][0] += data_train[i][0]*multiplier
				w[int(data_train[i][2])][1] += data_train[i][1]*multiplier
				w[int(data_train[i][2])][2] += 1*multiplier
				w[pos][0] -= data_train[i][0]*multiplier
				w[pos][1] -= data_train[i][1]*multiplier
				w[pos][2] -= 1*multiplier
	temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(common.constants.TEST_SIZE):
		for j in range(common.constants.NUM_CLASSES):
			temp[j] = w[j][0]*data_test[i][0] + w[j][1]*data_test[i][1]  + w[j][2]
		new = temp.index(max(temp))
		data_test[i][2] = new
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in
	# index 0 and Y in index 1, and a blank space in index 2
	# to be filled with class
	# The class value could be a 0 or a 8
	return
