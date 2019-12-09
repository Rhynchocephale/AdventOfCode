data = 'ne,ne,sw,sw,s'
data = data.split(',')

opposite = {'n':'s','s':'n','ne':'sw','sw':'ne','nw':'se','se':'nw'}

countedData = dict()
for key in opposite:
	countedData[key] = data.count(key)

print(countedData)

def reduced(data):
	for key in data:
		data[key], data[opposite[key]] = data[key] - min(data[key], data[opposite[key]]), data[opposite[key]] - min(data[key], data[opposite[key]])
	return data
	
print(reduced(countedData))
		
