data, recipes, elf1, elf2 = '409551', '37', 0, 1

while True:
	recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
	elf1 = (1+elf1+int(recipes[elf1]))%len(recipes)
	elf2 = (1+elf2+int(recipes[elf2]))%len(recipes)
	if data in recipes[-len(data)-2:]:
		print(len(recipes.split(data)[0]))
		break
