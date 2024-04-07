import common
def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	for i in range(common.constants.MAP_HEIGHT):
		for j in range(common.constants.MAP_WIDTH):
			if map[i][j] == 2:
				map[i][j] = 4;
				start = (i ,j);
	found = dfs(start, map)
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

def dfs(node, map):
	y = node[0]
	x = node[1]
	if map[y][x] == 3:
		map[y][x] = 5
		return 1
	map[y][x] = 4
	children = fillChildren(node, map)
	for i in children:
		if dfs(i, map):
			map[y][x] = 5
			return 1
	return 0

def bf_search(map):
	found = False;
	# PUT YOUR CODE HERE
	parentMap = []
	for i in range(common.constants.MAP_HEIGHT):
		parentMap.append([])
		for j in range(common.constants.MAP_WIDTH):
			parentMap[i].append(0)
			if map[i][j] == 2:
				start = (i ,j)
				position = start
	queue = [start]
	while len(queue)>0:
		node = queue[0]
		y = node[0]
		x = node[1]
		if map[y][x] == 3:
			end = node
			map[y][x] = 5
			found = True
			break
		map[y][x] = 4
		children = fillChildren(node, map)
		parent = node
		for i in children:
			parentMap[i[0]][i[1]] = parent
			queue.append(i)
		queue.pop(0)
	if found:
		parent = parentMap[end[0]][end[1]]
		while parent != 0:
			map[parent[0]][parent[1]] = 5
			parent = parentMap[parent[0]][parent[1]]
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

def fillChildren(loc, map):
	direction = ['right', 'down', 'left', 'up']
	child = []
	y = loc[0]
	x = loc[1]
	for i in direction:
		if i == 'right':
			if x in range(0, common.constants.MAP_WIDTH - 1):
				if map[y][x+1] == 0 or map[y][x+1] == 3:
					child.append((y, x+1))
		elif i == 'down':
			if y in range(0, common.constants.MAP_HEIGHT - 1):
				if map[y+1][x] == 0 or map[y+1][x] == 3:
					child.append((y+1, x))
	 	elif i == 'left':
			if x in range(1, common.constants.MAP_WIDTH):
				if map[y][x-1] == 0 or map[y][x-1] == 3:
					child.append((y, x-1))
		elif i == 'up':
			if y in range(1, common.constants.MAP_HEIGHT):
				if map[y-1][x] == 0 or map[y-1][x] == 3:
					child.append((y-1, x))
	return child
