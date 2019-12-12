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

from math import gcd as pgcd

def countAsteroids(a,b):
	directions = set()
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == '.':
				continue
			if (i, j) == (a, b):
				continue
			div = pgcd(a-i, b-j)
			directions.add( ((a-i)//div, (b-j)//div) )
	
	return len(directions)

bestView = 0
d2 = []
for i in range(len(data)):
	s = ''
	for j in range(len(data[0])):
		if data[i][j] == '.':
			s += '.'
			continue
		view = countAsteroids(i,j)
		s += str(view)
		if view > bestView:
			bestView = view
	d2.append(s)

for line in d2:
	print(line)
print(bestView)
