import common
import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT
	# set line.m and line.b
	# to create an auxiliar bidimentional structure
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	space = common.init_space(2000, 2000)
	bmap = common.init_space(2000, 2000)
	mmap = common.init_space(2000, 2000)
	mVals = [float(i*0.01) for i in range(-1000,1000)]
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			color = [image[0][y][x], image[1][y][x], image[2][y][x]]
			if color == [0,0,0]:
				for i in range(2000):
					b = -x*mVals[i] + y
					if b<1000 and b>=-1000:
						space[int(b)+1000][i] += 1
						bmap[int(b)+1000][i] = b
						mmap[int(b)+1000][i] = mVals[i]
	votes = -1
	for j in range(len(space)):
		for i in range(len(space)):
			if space[j][i] > votes:
				votes = space[j][i]
				M = mmap[j][i]
				B = bmap[j][i]
	line.m=M
	line.b=B
	return line

def detect_normal(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT
	# set line.theta and line.r
	# to create an auxiliar bidimentional structure
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	space = common.init_space(1800, 1800)
	rmap = common.init_space(1800, 1800)
	thetamap = common.init_space(1800, 1800)
	thetas = [float(i*math.pi/1800) for i in range(0,1800)]
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			color = [image[0][y][x], image[1][y][x], image[2][y][x]]
			if color == [0,0,0]:
				for i in range(1800):
					r = x*math.cos(thetas[i]) + y*math.sin(thetas[i])
					if r<900 and r>=-900:
						space[int(r)+900][i] += 1
						rmap[int(r)+900][i] = r
						thetamap[int(r)+900][i] = thetas[i]
	votes = -1
	for j in range(len(space)):
		for i in range(len(space)):
			if space[j][i] > votes:
				votes = space[j][i]
				R = rmap[j][i]
				THETA = thetamap[j][i]
	line.r=R
	line.theta=THETA
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT
	# to create an auxiliar bidimentional structure
	# you can use "space=common.init_space(heigh, width)"
	rad = 30
	space = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	edge = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	max = 0
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if isbackground(y, x, image) == False:
				if isedge(y, x, image):
					edge[y][x] = 1
					for j in range(y-rad,y+rad):
						for i in range(x-rad,x+rad):
							if isbackground(j,i,image) == False and distance(y,x,j,i) == 900:
								space[j][i] += 1
								if space[j][i] > max:
									max = space[j][i]
	count = 0
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if space[y][x] == max:
				count += 1
	return count

def distance(y,x,j,i):
	return ((y-j)**2 + (x-i)**2)

def isedge(y, x, image):
	if isbackground(y-1, x-1, image):
		return True
	elif isbackground(y-1, x, image):
		return True
	elif isbackground(y-1, x+1, image):
		return True
	elif isbackground(y, x+1, image):
		return True
	elif isbackground(y+1, x+1, image):
		return True
	elif isbackground(y+1, x, image):
		return True
	elif isbackground(y+1, x-1, image):
		return True
	elif isbackground(y, x-1, image):
		return True
	return False

def isbackground(y, x, image):
	if x<0 or x>common.constants.WIDTH-1 or y<0 or y>common.constants.HEIGHT-1:
		return True
	elif [image[0][y][x], image[1][y][x], image[2][y][x]] == [255, 255, 255]:
		return True
	return False
