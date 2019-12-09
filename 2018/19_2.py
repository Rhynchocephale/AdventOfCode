data = '''#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5'''

data = '''#ip 2
addi 2 16 2
seti 1 0 1
seti 1 3 3
mulr 1 3 5
eqrr 5 4 5
addr 5 2 2
addi 2 1 2
addr 1 0 0
addi 3 1 3
gtrr 3 4 5
addr 2 5 2
seti 2 6 2
addi 1 1 1
gtrr 1 4 5
addr 5 2 2
seti 1 1 2
mulr 2 2 2
addi 4 2 4
mulr 4 4 4
mulr 2 4 4
muli 4 11 4
addi 5 6 5
mulr 5 2 5
addi 5 19 5
addr 4 5 4
addr 2 0 2
seti 0 7 2
setr 2 6 5
mulr 5 2 5
addr 2 5 5
mulr 2 5 5
muli 5 14 5
mulr 5 2 5
addr 4 5 4
seti 0 7 0
seti 0 3 2'''

data = data.split('\n')
registerPointer = int(data[0].split()[1])
for i in range(1,len(data)):
	data[i-1] = data[i].split()
	data[i-1][1] = int(data[i-1][1])
	data[i-1][2] = int(data[i-1][2])
	data[i-1][3] = int(data[i-1][3])
data.pop()

import copy, random

registers = [0, 0, 0, 0, 0, 0]

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
	
functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def myfunction(x, registers):
	return eval(x[0])(x[1], x[2], x[3], registers)

registers[0] = 1
count = 0
while True:
	try:
		registers = myfunction(data[registers[registerPointer]], registers)
		#print(registers)
		if registers[registerPointer] > len(data):
			break
		else:
			registers[registerPointer] += 1
	except IndexError:
		break
	count += 1
	print(count, registers)

print(registers)
