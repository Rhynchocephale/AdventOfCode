def isValid(p):
	if hasAdjacent(p) and isIncreasing(p):
		return True
	return False

def hasAdjacent(p):
	q = str(p)
	for i in range(10):
		if 2*str(i) in q and not 3*str(i) in q:
			return True
	return False
	
def isIncreasing(p):
	return str(p) == ''.join(sorted(str(p)))

s=0
for i in range(145852,616942+1):
	if isValid(i):
		s+=1

print(s)
