#cave = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######""" 

#cave = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

#cave = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

cave="""################################
#########.####...#####.#########
#####...#G...#.G.##.#...##.##..#
####...G####.G....#..........E.#
#####..#######.................#
#####..###########.............#
#GG...############.............#
#...#.#.##..######..........#..#
##............#G.#..E.......####
##.G........#....#.........#####
###....G...................#####
###............G.....G.......###
#####.....#..G#####..........###
####..#......#######G...#.E..E##
####G##.G...#########.#.......##
###..###....#########...E....###
##...G......#########.E...######
##G.........#########......#####
##...#.G....#########.#...######
##...#.......#######E.##########
####.#........#####...##########
#######............E..##########
####..#...........E#############
##...G#...........##############
##........#.......##############
#####G..###..E..################
##########......################
##########.....#################
#########......#################
###########.....################
###########...##################
################################"""

cave = [list(x) for x in cave.split('\n')]

import copy, time

units = []
ID = 0
attackPower = 3
HP = 200
for x in range(len(cave)):
	for y in range(len(cave[x])):
		if cave[x][y] in ['E', 'G']:
			units.append([x, y, HP, cave[x][y], True])
			cave[x][y] = '.'
			ID+=1

def getEnemies(side, units):
	enemies = []
	for unit in units:
		if unit[3] != side and unit[4]:
			enemies.append(unit)
	return enemies
	
def orderSquares(squares):
	return sorted(squares, key=lambda unit: 1000*unit[0]+unit[1])
	
def touchingEnemies(unit, enemies):
	touching = []
	for coords in around(unit):
		for enemy in enemies:
			if enemy[0] == coords[0] and enemy[1] == coords[1]:
				touching.append(enemy)
	return touching
	
def movement(i, units, enemies, cave):
	unit = units[i]
	touching = touchingEnemies(units[i], enemies)
	if any(touching):
		return units
	
	whereToGo = destination(i, units, enemies, cave)
	if whereToGo:
		units[i] = [whereToGo[0], whereToGo[1], units[i][2], units[i][3], units[i][4]]
	
	return units

def destination(i, units, enemies, cave):
	emptyBlocs = []
	drawn = drawCave(units, cave)
	for enemy in enemies:
		for bloc in emptyNeighbours(enemy, drawn):
			if not bloc in emptyBlocs:
				emptyBlocs.append(bloc)
	
	minDist = 1000
	squareToGo = []
	for bloc in emptyBlocs:
		dist, square = path([units[i][0], units[i][1]], bloc, drawn)
		if dist > 0:
			if dist < minDist:
				minDist = dist
				squareToGo = [square]
			elif dist == minDist:
				squareToGo.append(square)
	if squareToGo:
		squareToGo = orderSquares(squareToGo)
		return squareToGo[0]
	return []

def around(unit):
	return [[unit[0]-1,unit[1]], [unit[0], unit[1]-1], [unit[0], unit[1]+1], [unit[0]+1, unit[1]]]

def emptyNeighbours(unit, cave):
	empty = []
	for coords in around(unit):
		try:
			if cave[coords[0]][coords[1]] not in ['#','E','G']:
				empty.append(coords)
		except IndexError:
			pass
	return empty

def path(init, dest, drawn2):
	drawn = copy.deepcopy(drawn2)
	drawn[init[0]][init[1]] = "."
	drawn[dest[0]][dest[1]] = 0
	hasChanged = True
	while hasChanged:
		hasChanged = False
		for i in range(len(drawn)):
			for j in range(len(drawn[i])):
				if drawn[i][j] in ['#','E','G'] or isinstance(drawn[i][j], int):
					continue
				mini = 10000
				for k in emptyNeighbours([i,j], drawn):
					if isinstance(drawn[k[0]][k[1]], int):
						if drawn[k[0]][k[1]] < mini:
							mini = drawn[k[0]][k[1]]
				if mini != 10000:
					hasChanged = True
					drawn[i][j] = mini+1
					#for line in drawn:
					#	print(''.join([str(x) for x in line]))
					#print()

	if isinstance(drawn[init[0]][init[1]], int):
		mini = 10000
		square = []
		for k in emptyNeighbours([init[0], init[1]], drawn):
			try:
				if drawn[k[0]][k[1]] < mini:
					square = k
					mini = drawn[k[0]][k[1]]
			except TypeError:
				pass
				
		return drawn[init[0]][init[1]], square
	return -1, []

def drawCave(units, cave):
	drawn = copy.deepcopy(cave)
	for unit in units:
		if unit[4]:
			drawn[unit[0]][unit[1]] = unit[3]
	return drawn
	
def endEverything(units, turn):
	print('FINI')
	somme = 0
	for unit in orderSquares(units):
		if unit[4]:
			somme += unit[2]
			print(unit[2])
	print()
	print(somme)
	print(turn)
	print(somme*turn)
	exit()

def attack(i, units, enemies):
	targets = touchingEnemies(units[i], enemies)
	if not any(targets):
		return units

	target = targets[0]
	for possibleTarget in targets:
		if possibleTarget[2] < target[2]:
			target = possibleTarget
			
	for unit in units:
		if target[0] == unit[0] and target[1] == unit[1]:
			unit[2] -= attackPower
			if unit[2] < 1:
				unit[2] = 0
				unit[4] = False
			return units

def completeTurn(units, cave, turn):
	units = orderSquares(units)
	for i in range(len(units)):
		if not units[i][4]:
			continue

		enemies = getEnemies(units[i][3], units)
		if not enemies:
			endEverything(units, turn)

		units = movement(i, units, enemies, cave)
		units = attack(i, units, enemies)
	return units

turn = 0
while True:
	print(turn)
	for line in drawCave(units, cave):
		print(''.join(line))
	print('----------')
	units = completeTurn(units, cave, turn)
	turn += 1

