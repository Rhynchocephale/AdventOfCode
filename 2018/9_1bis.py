import collections

players = 424
last = 71144*100

def game(players, last):
	circle = collections.deque([0])
	scores = [0]*players
	for i in range(1,last+1):
		if i%23:
			circle.rotate(-1)
			circle.append(i)
		else:
			circle.rotate(7)
			scores[i%players] += circle.pop() + i
			circle.rotate(-1)
	return scores
	
print(max(game(players, last)) )
