positions = [[17,-7,-11], [1,4,-1], [6,-2,-6], [19,11,9]]
#positions = [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]
velocity = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

import itertools

def gravity(positions, velocity):
	acceleration = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	for moons in itertools.combinations([x for x in range(len(positions))],2):
		a0, a1 = accelerate(moons, positions, velocity)
		acceleration[moons[0]] = addVector(acceleration[moons[0]], a0)
		acceleration[moons[1]] = addVector(acceleration[moons[1]], a1)
	for moon in range(len(positions)):
		velocity[moon] = addVector(velocity[moon], acceleration[moon])
	return velocity
	
def accelerate(moons, positions, velocity):
	a0, a1 = [0,0,0], [0,0,0]
	for dim in range(len(positions[0])):
		if positions[moons[0]][dim] > positions[moons[1]][dim]:
			a0[dim] = -1
			a1[dim] = 1
		elif positions[moons[0]][dim] < positions[moons[1]][dim]:
			a0[dim] = 1
			a1[dim] = -1	
	return a0, a1		

def move(positions, velocity):
	for i in range(len(positions)):
		positions[i] = addVector(positions[i], velocity[i])
	return positions

def addVector(a, b):
	for i in range(len(a)):
		a[i] += b[i]
	return a

def systemEnergy(positions, velocity):
	totalEnergy = 0
	for moon in range(len(positions[0])+1):
		totalEnergy += partialEnergy(positions[moon]) * partialEnergy(velocity[moon])
	return totalEnergy
	
def partialEnergy(a):
	somme = 0
	for x in a:
		somme += abs(x)
	return somme

def oneSecond(positions, velocity):
	velocity = gravity(positions, velocity)
	positions = move(positions, velocity)
	return positions, velocity
	
for i in range(1001):
	'''print(i)
	for moon in range(len(positions)):
		print(positions[moon], velocity[moon])'''
	print(i,systemEnergy(positions, velocity))
	positions, velocity = oneSecond(positions, velocity)
