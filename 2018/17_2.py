f = open('a.txt','r')
g = open('b.txt','w')

for line in f:
	lineOld = line
	lineNew = line.replace('.2','..').replace('2.','..').replace('2\n','.\n')
	while lineOld != lineNew:
		lineOld = lineNew
		lineNew = lineOld.replace('.2','..').replace('2.','..').replace('2\n','.\n')
	g.write(lineNew)

f.close()
g.close()

g = open('b.txt','r')
t = '\n'.join(g.readlines())
print(t.count('2'))
