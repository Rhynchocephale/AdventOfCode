import time

players = 424
lastMarble = 71144*100
scores = [0]*players

def insertMarble(marble, currentMarble, circle, currentPlayer, scores):
	if not marble%23:
		return insert23Marble(marble, currentMarble, circle, currentPlayer, scores)
	
	whereToInsert = circle.index(currentMarble)+2
	if whereToInsert > len(circle):
		whereToInsert -= len(circle)
	circle.insert(whereToInsert, marble)
	
	return marble, circle, scores

def insert23Marble(marble, currentMarble, circle, currentPlayer, scores):
	whereToRemove = circle.index(currentMarble)-7
	if whereToRemove < 0:
		whereToRemove += len(circle)
		
	scores[currentPlayer-1] += circle.pop(whereToRemove) + marble
	return circle[whereToRemove], circle, scores

circle = [0,2,1,3]
currentPlayer = 4
currentMarble = 3
startTime = time.time()
now = time.time()
for i in range(currentMarble+1,lastMarble+1):
	if not i%10000:
		lapDuration = time.time()-now
		now = time.time()
		totalElapsed = now-startTime
		print(i, round(totalElapsed, 2), round(lapDuration, 2))
	currentMarble, circle, scores = insertMarble(i, currentMarble, circle, currentPlayer, scores)
	#print("["+str(currentPlayer)+"] "+" ".join([str(x) for x in circle]))
	currentPlayer += 1
	if currentPlayer > players:
		currentPlayer = 1
	
print(max(scores))
