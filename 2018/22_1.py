depth = 9465
target = [13,704]

#depth = 510
#target = [10,10]

m = 20183

import numpy as np

geologic_grid = np.full([x+1 for x in target], -1)
erosion_grid = np.full([x+1 for x in target], -1)

geologic_grid[0][0] = 0
geologic_grid[target[0]][target[1]] = 0

def geologic(x, y, geo_grid, ero_grid):
	if geo_grid[x][y] != -1:
		return geo_grid[x][y]
	if x == 0:
		return y*48271
	if y == 0:
		return x*16807

	return erosion(x-1, y, geo_grid, ero_grid)*erosion(x, y-1, geo_grid, ero_grid)
		
def erosion(x, y, geo_grid, ero_grid):
	if ero_grid[x][y] != -1:
		return ero_grid[x][y]
		
	return (geologic(x, y, geo_grid, ero_grid)+depth)%20183

for x in range(target[0]+1):
	for y in range(target[1]+1):
		geologic_grid[x][y] = geologic(x, y, geologic_grid, erosion_grid)
		erosion_grid[x][y] = erosion(x, y, geologic_grid, erosion_grid)

somme = 0
drawn = ''
for x in range(target[0]+1):
	for y in range(target[1]+1):
		somme += erosion_grid[x][y]%3
		if erosion_grid[x][y]%3 == 0:
			drawn+='.'
		elif erosion_grid[x][y]%3 == 1:
			drawn+='='
		else:
			drawn+='|'
	drawn += '\n'

print(geologic_grid[1][0])
print(erosion_grid[1][0])
print(drawn)
print(somme)
