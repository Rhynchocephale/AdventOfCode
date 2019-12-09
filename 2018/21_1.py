data = '''#ip 4
seti 123 0 5
bani 5 456 5
eqri 5 72 5
addr 5 4 4
seti 0 0 4
seti 0 9 5
bori 5 65536 3
seti 10828530 0 5
bani 3 255 2
addr 5 2 5
bani 5 16777215 5
muli 5 65899 5
bani 5 16777215 5
gtir 256 3 2
addr 2 4 4
addi 4 1 4
seti 27 4 4
seti 0 4 2
addi 2 1 1
muli 1 256 1
gtrr 1 3 1
addr 1 4 4
addi 4 1 4
seti 25 9 4
addi 2 1 2
seti 17 9 4
setr 2 8 3
seti 7 9 4
eqrr 5 0 2
addr 2 4 4
seti 5 5 4'''

data = data.split('\n')
registerPointer = int(data[0].split()[1])
for i in range(1,len(data)):
	data[i-1] = data[i].split()
	data[i-1][1] = int(data[i-1][1])
	data[i-1][2] = int(data[i-1][2])
	data[i-1][3] = int(data[i-1][3])
data.pop()

import copy

def addr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] + r[b]
	return r
	
def addi(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] + b
	return r
	
def mulr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] * r[b]
	return r
	
def muli(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] * b
	return r

def banr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] & r[b]
	return r
	
def bani(a, b, c, registers):
	r = copy.deepcopy(registers)	
	r[c] = r[a] & b
	return r

def borr(a, b, c, registers):
	r = copy.deepcopy(registers)	
	r[c] = r[a] | r[b]
	return r
	
def bori(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] | b
	return r

def setr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a]
	return r

def seti(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a
	return r
	
def gtir(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a > r[b]
	return r
	
def gtri(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] > b
	return r

def gtrr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] > r[b]
	return r

def eqir(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a == r[b]
	return r
	
def eqri(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == b
	return r

def eqrr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == r[b]
	return r

def myfunction(x, registers):
	return eval(x[0])(x[1], x[2], x[3], registers)

results = []
maxIter = 100000
value0 = 0
while value0 < 1000:
	registers = [value0, 0, 0, 0, 0, 0]
	
	count = 0
	while count < maxIter:
		try:
			registers = myfunction(data[registers[registerPointer]], registers)
			if registers[registerPointer] > len(data):
				break
			else:
				registers[registerPointer] += 1
		except IndexError:
			break
		count += 1
	
	if count < maxIter:
		print(value0, count)
		results.append([value0, count])
	value0 += 1
	
print(results)
