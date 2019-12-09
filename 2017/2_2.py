somme = 0

with open('2_1.txt','r') as f:
	for line in f:
		g = sorted([int(x) for x in line.split()])
		somme += g[-1]-g[0]

print(somme)
