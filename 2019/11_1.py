#data = [1102,34915192,34915192,7,4,7,99,0]
#data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
data = [3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

relative = 0

from itertools import permutations

def avoidKeyErrors(data, index):
	for i in [index+1, index+2, index+3]:
		if not i in data and i >= 0:
			data[i] = 0
	for i in [data[index+1], data[index+2], data[index+3], data[index+1]+relative, data[index+2]+relative, data[index+3]+relative]:
		if not i in data and i >= 0:
			data[i] = 0
	return data

def browseData(data, index):
	global relative, out
	
	code, mode = getModes(data[index])
	data = avoidKeyErrors(data, index)
	
	if mode[0] == '0':
		i1 = data[index+1]
	elif mode[0] == '1':
		i1 = index+1
	elif mode[0] == '2':
		i1 = data[index+1]+relative
		
	if mode[1] == '0':
		i2 = data[index+2]
	elif mode[1] == '1':
		i2 = index+2
	elif mode[1] == '2':
		i2 = data[index+2]+relative
	
	if mode[2] == '0':
		i3 = data[index+3]
	elif mode[2] == '1':
		i3 = index+3
	elif mode[2] == '2':
		i3 = data[index+3]+relative
	
	if code == 1:
		data[i3] = data[i1] + data[i2]
		return data, index+4
	elif code == 2:
		data[i3] = data[i1] * data[i2]
		return data, index+4
	elif code == 3:
		#data[index+1] = input()
		data[i1] = inp
		return data, index+2
	elif code == 4:
		out.append(data[i1])
		return data, index+2
	elif code == 5:
		if data[i1] != 0:
			return data, data[i2]
		return data, index+3
	elif code == 6:
		if data[i1] == 0:
			return data, data[i2]
		return data, index+3
	elif code == 7:
		data[i3] = int(data[i1] < data[i2])
		return data, index+4
	elif code == 8:
		data[i3] = int(data[i1] == data[i2])
		return data, index+4
	elif code == 9:
		relative += data[i1]
		return data, index+2
	elif code == 99:
		print(len(painted))
		exit()
	else:
		print('olala')
		exit()
	
def getModes(n):
	instr = str(n)
	if len(instr) <= 2:
		return n, '000'
	code = int(instr[-2:])
	mode = instr[:-2]
	mode = mode.zfill(3)[::-1]
	return code, mode
	
def arrayToDict(l):
	d = dict()
	for i in range(len(l)):
		d[i] = l[i]
	return d
	
def makeGrid():
	d = dict()
	d[(0,0)] = '.'
	return d

def paint(painted, position, grid, colour):
	painted.add(position)
	grid[position] = ['.','#'][colour]
	return painted, grid
	
def move(position, direction, grid, turn):
	if turn == 0:
		if direction == (0,1):
			direction = (-1,0)
		elif direction == (-1,0):
			direction = (0,-1)
		elif direction == (0,-1):
			direction = (1,0)
		elif direction == (1,0):
			direction = (0,1)
	elif turn == 1:
		if direction == (0,1):
			direction = (1,0)
		elif direction == (1,0):
			direction = (0,-1)
		elif direction == (0,-1):
			direction = (-1,0)
		elif direction == (-1,0):
			direction = (0,1)
	
	position = (position[0]+direction[0], position[1]+direction[1])
	if not position in grid:
		grid[position] = '.'
	return position, direction
	
def getInp(grid, position):
	colour = grid[position]
	if colour == '.':
		return 0
	return 1
	
index = 0
out = []
data = arrayToDict(data)
grid = makeGrid()
position = (0,0)
direction = (0,1)
painted = set()
inp = getInp(grid, position)
while True:
	data, index = browseData(data, index)
	if len(out) == 2:
		painted, grid = paint(painted, position, grid, out[0])
		position, direction = move(position, direction, grid, out[1])
		inp = getInp(grid, position)
		out = []
	
