data = 409551

recipes = [3, 7]
elves = [0, 1]

def digits(v):
	return [int(x) for x in str(sum(v))]
	

def tick(recipes, elves):
	recipes += digits([recipes[elf] for elf in elves])
	
	for i in range(len(elves)):
		elves[i] = (1+elves[i]+recipes[elves[i]])%len(recipes)

	return recipes, elves
	

while len(recipes) < data+10:
	recipes, elves = tick(recipes, elves)

print('---')
print(''.join([str(x) for x in recipes[data:data+10]]))
