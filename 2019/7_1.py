data = [3,8,1001,8,10,8,105,1,0,0,21,46,59,80,105,122,203,284,365,446,99999,3,9,102,3,9,9,1001,9,5,9,102,2,9,9,1001,9,3,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,4,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,102,5,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]

from itertools import permutations

def browseData(data, index, inp, first3):
	code, mode = getModes(data[index])
		
	if code == 1:
		if mode == '00':
			data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
		elif mode == '01':
			data[data[index+3]] = data[data[index+1]] + data[index+2]
		elif mode == '10':
			data[data[index+3]] = data[index+1] + data[data[index+2]]
		elif mode == '11':
			data[data[index+3]] = data[index+1] + data[index+2]
		return data, index+4, first3
	elif code == 2:
		if mode == '00':
			data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
		elif mode == '01':
			data[data[index+3]] = data[data[index+1]] * data[index+2]
		elif mode == '10':
			data[data[index+3]] = data[index+1] * data[data[index+2]]
		elif mode == '11':
			data[data[index+3]] = data[index+1] * data[index+2]
		return data, index+4, first3
	elif code == 3:
		#data[index+1] = input()
		data[data[index+1]] = inp[not first3]
		return data, index+2, not first3
	elif code == 4:
		if mode == '0':
			'''print('###########')
			print(data[data[index+1]])
			print('###########')'''
			return data[data[index+1]], -1, first3
		elif mode == '1':
			'''print('###########')
			print(data[index+1])
			print('###########')'''
			return data[index+1], -1, first3
		#return data, index+2
	elif code == 5:
		if mode == '00':
			if data[data[index+1]] != 0:
				return data, data[data[index+2]], first3
		elif mode == '01':
			if data[data[index+1]] != 0:
				return data, data[index+2], first3
		elif mode == '10':
			if data[index+1] != 0:
				return data, data[data[index+2]], first3
		elif mode == '11':
			if data[index+1] != 0:
				return data, data[index+2], first3
		return data, index+3, first3
	elif code == 6:
		if mode == '00':
			if data[data[index+1]] == 0:
				return data, data[data[index+2]], first3
		elif mode == '01':
			if data[data[index+1]] == 0:
				return data, data[index+2], first3
		elif mode == '10':
			if data[index+1] == 0:
				return data, data[data[index+2]], first3
		elif mode == '11':
			if data[index+1] == 0:
				return data, data[index+2], first3
		return data, index+3, first3
	elif code == 7:
		if mode == '00':
			data[data[index+3]] = int(data[data[index+1]] < data[data[index+2]])
		elif mode == '01':
			data[data[index+3]] = int(data[data[index+1]] < data[index+2])
		elif mode == '10':
			data[data[index+3]] = int(data[index+1] < data[data[index+2]])
		elif mode == '11':
			data[data[index+3]] = int(data[index+1] < data[index+2])
		return data, index+4, first3
	elif code == 8:
		if mode == '00':
			data[data[index+3]] = int(data[data[index+1]] == data[data[index+2]])
		elif mode == '01':
			data[data[index+3]] = int(data[data[index+1]] == data[index+2])
		elif mode == '10':
			data[data[index+3]] = int(data[index+1] == data[data[index+2]])
		elif mode == '11':
			data[data[index+3]] = int(data[index+1] == data[index+2])
		return data, index+4, first3
	elif code == 99:
		exit()
	else:
		print('olala')
		return 1
	
def getModes(n):
	instr = str(n)
	if len(instr) <= 2:
		if n in [3,4]:
			return n, '0'
		return n, '00'
	code = int(instr[-2:])
	mode = instr[:-2]
	if code in [1,2,5,6,7,8]:
		mode = mode.zfill(2)
		mode = mode[1]+mode[0]
	elif code in [3,4]:
		mode = mode.zfill(1)
	return code, mode

phases = permutations([0,1,2,3,4], 5)

maxOut = 0
for phase in phases:
	out = 0
	for setting in phase:
		data0 = data[:]
		index = 0
		inp = [setting, out]
		print(inp)
		first3 = True
		while True:
			data0, index, first3 = browseData(data0, index, inp, first3)
			#print(data0, index)
			if index == -1:
				out = data0
				if out > maxOut:
					maxOut = out
				break

print(maxOut)
