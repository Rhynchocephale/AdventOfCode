data = '''357, 59
312, 283
130, 47
89, 87
87, 58
158, 169
182, 183
300, 318
82, 257
200, 194
71, 259
112, 67
82, 163
107, 302
58, 194
40, 88
288, 339
64, 245
243, 302
41, 43
147, 276
143, 116
103, 178
262, 226
253, 157
313, 71
202, 236
353, 192
96, 74
167, 50
125, 132
90, 315
174, 232
185, 237
126, 134
152, 191
104, 315
283, 90
95, 193
252, 286
48, 166
69, 75
48, 349
59, 124
334, 95
263, 134
50, 314
196, 66
342, 221
60, 217'''

import numpy as np

data = sorted(data.split('\n'))
data = np.array([[int(data[_].split(', ')[0]), int(data[_].split(', ')[1]), _] for _ in range(len(data))])

minX, minY, maxX, maxY = 0, 0, max(data[:,0]), max(data[:,1])

grid = np.empty((maxX+1, maxY+1))

def manhattan(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def closestPoint(p1):
	minDist = 2*(maxX+maxY)
	isSplit = False
	closest = -1
	for p2 in data:
		dist = manhattan(p1, p2)
		if dist < minDist:
			minDist = dist
			closest = p2[2]
			isSplit = False
		elif dist == minDist:
			isSplit = True
	
	if isSplit:
		return -1
	return closest

def areaSize(num):
	return np.count_nonzero(grid == num)
	
def getBorders(grid):
	return set(grid[0,:]).union(set(grid[-1,:])).union(set(grid[:,0])).union(set(grid[:,-1]))

def getNonInfinite(grid):
	return set(np.unique(grid)).difference(getBorders(grid)).difference(set([-1]))

for x in range(len(grid)):
	for y in range(len(grid[0])):
		grid[x,y] = closestPoint([x,y])

maxSize = 0
for num in getNonInfinite(grid):
	size = areaSize(num)
	if size > maxSize:
		maxSize = size
		
print(maxSize)
