status = "#...#..##.......####.#..###..#.##..########.#.#...#.#...###.#..###.###.#.#..#...#.#..##..#######.##"

data = """#..#. => #
#.#.. => #
###.. => #
##..# => .
.#.## => #
..... => .
...#. => #
##.#. => #
#.#.# => .
###.# => #
....# => .
####. => #
.##.. => #
#.##. => #
#..## => #
##... => #
#...# => .
##.## => #
.#... => .
.#..# => #
..#.# => #
##### => .
.#### => #
..#.. => #
#.### => .
..##. => .
.##.# => #
.#.#. => .
..### => .
.###. => .
...## => .
#.... => ."""

generations = 20

import collections

data = [line.split(' => ') for line in data.split('\n')]
data = [x[0] for x in data if x[1]=='#']
print(data)

def printStatus(status, index=False):
	if index:
		print(''.join([status[i-2][1], status[i-1][1], status[i][1], status[i+1][1], status[i+2][1]]))
	else:
		print(' '.join([x[1] for x in status]))
		print(' '.join([str(x[0]) for x in status]))

status = collections.deque(status)
for i in range(len(status)):
	status[i] = [i, status[i]]

def enlargeStatus(status):
	maxNb = status[-1][0]
	minNb = status[0][0]	
	status.appendleft([minNb-1, '.'])
	status.appendleft([minNb-2, '.'])
	status.appendleft([minNb-3, '.'])
	status.append([maxNb+1, '.'])
	status.append([maxNb+2, '.'])
	status.append([maxNb+3, '.'])
	
	#printStatus(status)
	
	return truncateStatus(status)
	
def truncateStatus(status):
	a = 0
	for i in range(len(status)):
		if status[i][1] != '.':
			a = i
			break
	if a:
		for i in range(3,a):
			status.popleft()
		
	a = 0
	for i in range(len(status)-1,0,-1):
		if status[i][1] != '.':
			a = i
			break
	if a:
		for i in range(a+3,len(status)-1):
			status.pop()
	
	return status

def iteration(status, data):
	newStatus = collections.deque([[x[0], x[1]] for x in status])
	
	for i in range(2,len(status)-2):
		for pattern in data:
			if matchPattern(i, pattern, status):
				newStatus[i] = [newStatus[i][0], '#']
				break
		else:
			newStatus[i] = [newStatus[i][0], '.']
		
	return newStatus

def matchPattern(i, pattern, status):
	if status[i-2][1] == pattern[0] and status[i-1][1] == pattern[1] and status[i][1] == pattern[2] and status[i+1][1] == pattern[3] and status[i+2][1] == pattern[4]:
		return True
	return False
	
def printSum(status):
	somme = 0
	for x in status:
		if x[1] == '#':
			print(x)
			somme += x[0]
	print(somme)


for i in range(generations):
	status = iteration(enlargeStatus(status), data)
	print('GENERATION', i+1)
	printStatus(status)
	printSum(status)
