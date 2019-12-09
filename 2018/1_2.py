f = open('1_1.txt','r')
g = f.readlines()
f.close()

for i in range(len(g)):
	g[i] = int(g[i].replace('\n',''))
	
found = set()
found.add(0)

current = 0
i = 0
while True:
	for x in g:
		i+=1
		current += x
		if current in found:
			print(current)
			print(i)
			exit()
		else:
			found.add(current)
