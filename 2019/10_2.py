data = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''
data=data.split('\n')

import math

def listAsteroids(a,b):
	directions = set()
	asteroids = dict()
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == '.':
				continue
			if (i, j) == (a, b):
				continue
			div = math.gcd(a-i, b-j)
			minVect = ((a-i)//div, (b-j)//div)
			directions.add( minVect )
			if minVect in asteroids:
				if a-i < a-asteroids[minVect][0]:
					asteroids[minVect] = [i,j]
			else:
				asteroids[minVect] = [i,j]
	return directions, asteroids

def toPolar(x):	
	coord = list(x)
	
	#translate
	coord[0] -= bestCoords[0]
	coord[1] -= bestCoords[1]
	
	#polarise
	rho = pow(coord[0]**2+coord[1]**2, 0.5)
	if coord[0] == 0:
		theta = math.pi/2
	else:
		theta = math.atan(coord[1]/coord[0])
	if coord[0] < 0:
		theta += math.pi
	elif coord[1] < 0:
		theta += 2*math.pi
	theta += math.pi
	theta = -theta
	theta %= 2*math.pi
	
	return theta		

def vaporiseOneRound(a,b,vaporised):
	global data
	
	directions, asteroids = listAsteroids(a,b)
	if not asteroids:
		print('Space has been cleared')
		exit()
	tmp = [x for x in list(asteroids.keys())]
	newOrder = sorted(tmp, key=toPolar)
	newOrder = sorted(newOrder, key=toPolar)
	for o in newOrder:
		print(asteroids[o], toPolar(asteroids[o]))
	for o in newOrder:
		vaporised += 1
		print(vaporised, asteroids[o])
		printSpace(asteroids[o])
		exit()
		data[asteroids[o][0]][asteroids[o][1]] = '.'
		if vaporised == 200:
			pass
			#exit()

	return vaporised

def printSpace(asteroid):
	data2 = [[x for x in line] for line in data]
	data2[asteroid[0]][asteroid[1]] = '1'
	data2[bestCoords[0]][bestCoords[1]] = 'X'
	
	for line in data2:
		print(''.join(line))

for i in range(len(data)):
	data[i] = list(data[i])

bestView = 0
d2 = []
for i in range(len(data)):
	s = ''
	for j in range(len(data[0])):
		if data[i][j] == '.':
			s += '.'
			continue
		directions, asteroids = listAsteroids(i,j)
		view = len(directions)
		s += str(view)
		if view > bestView:
			bestView = view
			bestCoords = (i, j)
	d2.append(s)

for line in d2:
	print(line)
print(bestView)
print(bestCoords)

i = 0
while True:
	i = vaporiseOneRound(bestCoords[0], bestCoords[1], i)
	
	#draw
	'''data2 = [[x for x in line] for line in data]
	data2[destroyed[0]][destroyed[1]] = '1'
	for line in data2:
		print(line)
	print('------------')'''

