data = 5177

def hundreds(a):
	try:
		h = str(a)[-3]
		return int(h)
	except IndexError:
		return 0

'''def bottomToTop(x, y):
	return x+1, 300-y

def topToBottom(i, j):
	return i-1, 300-j'''

def cellPower(i, j, data):
	return hundreds( ((i+10)*j+data)*(i+10) )-5

def getSquare(i, j, size):
	if i+size>300 or j+size>300:
		return []
	return [[i+a,j+b] for a in range(size) for b in range(size)]

def computeSquare(i, j, size, data):
	square = getSquare(i, j, size)
	somme = 0
	for x in square:
		somme += cellPower(x[0], x[1], data)
	return somme

maxi = 0
coord = [0, 0, 0]

for size in range(1,300):
	for i in range(1,300-size+1):
		for j in range(1,300-size+1):
			r = computeSquare(i, j, size, data)
			if r>maxi:
				maxi=r
				coord=[i, j, size]
	print(size)
	print(maxi, coord)
	print('----')

print('----------FIN-----------')
print(maxi, coord)
