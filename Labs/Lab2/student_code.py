import common
import collections

def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	parentMap = []
	gmap = []
	fmap = []
	for i in range(common.constants.MAP_HEIGHT):
		parentMap.append([])
		gmap.append([])
		fmap.append([])
		for j in range(common.constants.MAP_WIDTH):
			parentMap[i].append(0)
			gmap[i].append(0)
			fmap[i].append(0)
			if map[i][j] == 2:
				start = (i ,j)
				position = start
			elif map[i][j] == 3:
				end = (i, j)
	if end == 0:
		found = False
		return found
	queue = [start]
	fmap[start[0]][start[1]] = manhattan(start, end)
	nextNode = start
	while len(queue)>0:
		node = nextNode
		nodeIndex = queue.index(node)
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
			gn = 0
			parentMap[i[0]][i[1]] = parent
			temp = parentMap[i[0]][i[1]]
			while temp != 0:
				gn = gn + 1
				temp = parentMap[temp[0]][temp[1]]
			gmap[i[0]][i[1]] = gn
			fmap[i[0]][i[1]] = gmap[i[0]][i[1]] + manhattan(i, end)
			queue.append(i)
		queue.pop(nodeIndex)
		if len(queue) == 0:
			found = False
			break
		fminNode = queue[0]
		for i in queue:
			if fmap[i[0]][i[1]] < fmap[fminNode[0]][fminNode[1]]:
				fminNode = i
			elif fmap[i[0]][i[1]] == fmap[fminNode[0]][fminNode[1]]:
				if i[1] < fminNode[1]:
					fminNode = i
				elif i[1] == fminNode[1]:
					if i[0] < fminNode[0]:
						fminNode = i
			nextNode = fminNode
	if found:
		parent = parentMap[end[0]][end[1]]
		while parent != 0:
			map[parent[0]][parent[1]] = 5
			parent = parentMap[parent[0]][parent[1]]
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

def manhattan(node, end):
	ypos = node[0]
	xpos = node[1]
	yend = end[0]
	xend = end[1]
	return (abs(ypos-yend) + abs(xpos-xend))

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
