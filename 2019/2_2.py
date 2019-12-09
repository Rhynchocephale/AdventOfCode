data0 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0]

def browseData(data, index):
	if data[index] == 1:
		data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
		return data
	elif data[index] == 2:
		data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
		return data
	elif data[index] == 99:
		if data[0] == 19690720:
			return 0
		else:
			return 1
	else:
		return 1
		
for n in range(100):
	for v in range(100):
		index = 0
		data = [x for x in data0]
		data[1] = n
		data[2] = v
		while True:
			data = browseData(data, index)
			index += 4
			if data == 0:
				print(100*n+v)
				exit()
			elif data == 1:
				break
