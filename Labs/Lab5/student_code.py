import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	start = values_init(map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle)
	gamma = 1 - discount_per_cycle
	while(1):
		new = []
		diff = []
		make_copy(new, diff, values)
		for y in range(6):
			for x in range(6):
				pos = (y, x)
				if map[y][x] not in [2,3]:
					count = 1
					new[y][x] = get_value(count, gamma, pos, values, battery_drop_cost)
					policies[y][x] = 1
					while(count<=8):
						if new[y][x] < get_value(count, gamma, pos, values, battery_drop_cost):
							new[y][x] = get_value(count, gamma, pos, values, battery_drop_cost)
							policies[y][x] = count
						count = count + 1
				diff[y][x] = new[y][x] - values[y][x]
		make_values(values, new)
		if convergence(diff, new):
			return values[start[0]][start[1]]
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	#

def convergence(diff, new):
	total = 0.0
	change = 0.0
	for y in range(6):
		for x in range(6):
			total = total + abs(new[y][x])
			change =  change + abs(diff[y][x])
	if change/total <= 0.0001:
		return 1
	return 0

def make_values(values, new):
	for y in range(6):
		for x in range(6):
			values[y][x] = new[y][x]

def boundary(y, x):
	s = 0
	w = 0
	n = 0
	e = 0
	if y in range(1,5) and x in range(1, 5):
		s = 1
		w = 1
		n = 1
		e = 1
	if y in range(5):
		s = 1
	if x in range(1,6):
		w = 1
	if y in range(1,6):
		n = 1
	if x in range(5):
		e = 1
	return [s, w, n, e]

def get_value(count, gamma, pos, values, battery_drop_cost):
	y = pos[0]
	x = pos[1]
	mul = 1.0
	south, west, north, east = boundary(y, x)
	if count == 1:
		a = 0.70*values[y+south][x]
		b = 0.15*values[y][x-west]
		c = 0.15*values[y][x+east]
	elif count == 2:
		a = 0.70*values[y][x-west]
		b = 0.15*values[y-north][x]
		c = 0.15*values[y+south][x]
	elif count == 3:
		a = 0.70*values[y-north][x]
		b = 0.15*values[y][x-west]
		c = 0.15*values[y][x+east]
	elif count == 4:
		a = 0.70*values[y][x+east]
		b = 0.15*values[y-north][x]
		c = 0.15*values[y+south][x]
	elif count == 5:
		a = 0.80*values[y+south][x]
		b = 0.10*values[y][x-west]
		c = 0.10*values[y][x+east]
		mul = 2.0
	elif count == 6:
		a = 0.80*values[y][x-west]
		b = 0.10*values[y-north][x]
		c = 0.10*values[y+south][x]
		mul = 2.0
	elif count == 7:
		a = 0.80*values[y-north][x]
		b = 0.10*values[y][x-west]
		c = 0.10*values[y][x+east]
		mul = 2.0
	elif count == 8:
		a = 0.80*values[y][x+east]
		b = 0.10*values[y-north][x]
		c = 0.10*values[y+south][x]
		mul = 2.0
	return (gamma*(a + b + c) - mul*battery_drop_cost)

def make_copy(new, diff, values):
	for i in range(6):
		new.append([])
		diff.append([])
		for j in range(6):
			new[i].append(values[i][j])
			diff[i].append(0.0)

def values_init(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	for y in range(6):
		for x in range(6):
			if map[y][x] == common.constants.PIZZA:
				start = (y,x)
			elif map[y][x] == common.constants.CUSTOMER:
				values[y][x] = delivery_fee
			elif map[y][x] == common.constants.RIVAL:
				values[y][x] = -dronerepair_cost
	return start
