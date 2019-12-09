data = """Step O must be finished before step C can begin.
Step Y must be finished before step D can begin.
Step N must be finished before step D can begin.
Step G must be finished before step F can begin.
Step C must be finished before step Z can begin.
Step H must be finished before step K can begin.
Step W must be finished before step T can begin.
Step T must be finished before step F can begin.
Step S must be finished before step I can begin.
Step X must be finished before step B can begin.
Step J must be finished before step A can begin.
Step K must be finished before step D can begin.
Step Z must be finished before step A can begin.
Step A must be finished before step B can begin.
Step L must be finished before step V can begin.
Step F must be finished before step M can begin.
Step B must be finished before step V can begin.
Step M must be finished before step Q can begin.
Step D must be finished before step E can begin.
Step I must be finished before step U can begin.
Step R must be finished before step V can begin.
Step E must be finished before step U can begin.
Step P must be finished before step V can begin.
Step V must be finished before step Q can begin.
Step U must be finished before step Q can begin.
Step P must be finished before step U can begin.
Step O must be finished before step F can begin.
Step T must be finished before step M can begin.
Step I must be finished before step Q can begin.
Step M must be finished before step U can begin.
Step R must be finished before step E can begin.
Step T must be finished before step R can begin.
Step H must be finished before step S can begin.
Step L must be finished before step B can begin.
Step S must be finished before step Q can begin.
Step E must be finished before step Q can begin.
Step B must be finished before step Q can begin.
Step S must be finished before step M can begin.
Step C must be finished before step D can begin.
Step S must be finished before step R can begin.
Step G must be finished before step D can begin.
Step T must be finished before step E can begin.
Step T must be finished before step Q can begin.
Step N must be finished before step I can begin.
Step S must be finished before step P can begin.
Step N must be finished before step J can begin.
Step X must be finished before step L can begin.
Step G must be finished before step K can begin.
Step N must be finished before step E can begin.
Step H must be finished before step D can begin.
Step H must be finished before step P can begin.
Step O must be finished before step A can begin.
Step V must be finished before step U can begin.
Step F must be finished before step D can begin.
Step B must be finished before step P can begin.
Step T must be finished before step L can begin.
Step I must be finished before step P can begin.
Step K must be finished before step Z can begin.
Step G must be finished before step M can begin.
Step F must be finished before step Q can begin.
Step J must be finished before step L can begin.
Step H must be finished before step Q can begin.
Step W must be finished before step R can begin.
Step R must be finished before step U can begin.
Step P must be finished before step Q can begin.
Step D must be finished before step V can begin.
Step G must be finished before step C can begin.
Step Z must be finished before step B can begin.
Step O must be finished before step H can begin.
Step S must be finished before step A can begin.
Step J must be finished before step Q can begin.
Step N must be finished before step F can begin.
Step L must be finished before step R can begin.
Step O must be finished before step R can begin.
Step W must be finished before step M can begin.
Step J must be finished before step F can begin.
Step G must be finished before step W can begin.
Step K must be finished before step U can begin.
Step D must be finished before step U can begin.
Step W must be finished before step I can begin.
Step E must be finished before step V can begin.
Step Y must be finished before step Q can begin.
Step L must be finished before step E can begin.
Step S must be finished before step B can begin.
Step T must be finished before step V can begin.
Step C must be finished before step U can begin.
Step M must be finished before step P can begin.
Step G must be finished before step S can begin.
Step B must be finished before step R can begin.
Step K must be finished before step M can begin.
Step X must be finished before step A can begin.
Step R must be finished before step P can begin.
Step B must be finished before step I can begin.
Step C must be finished before step X can begin.
Step O must be finished before step P can begin.
Step D must be finished before step Q can begin.
Step F must be finished before step B can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step I can begin.
Step M must be finished before step D can begin.
Step F must be finished before step U can begin."""

data = data.replace('Step ','').replace(' must be finished before step', '').replace(' can begin.', '').split('\n')
data = [_.split() for _ in data]
stepsLeft = set([_[0] for _ in data]+[_[1] for _ in data])

availableWorkers = 5
stepDurationMalus = 60
workers = [['',0] for _ in range(availableWorkers)]
completed = []
ready = set()
elapsed = 0

def getReady(completed, stepsLefts):
	ready_tmp = set([_ for _ in stepsLeft])
	for x in data:
		if not x[0] in completed:
			try:
				ready_tmp.remove(x[1])
			except KeyError:
				pass
	return sorted(list(ready_tmp))

def stepDuration(letter):
	return ord(letter)-ord('A')+1+stepDurationMalus
			
def oneSecond(workers):
	return [[x[0], x[1]-(x[1]>0)] for x in workers]
	
def assignWorker(lst, letter):
	if letter:
		for i in range(len(lst)):
			if lst[i][1] == 0:
				lst[i] = [letter, stepDuration(letter)]
				return lst
	else:
		for i in range(len(lst)):
			if lst[i][1] == 0:
				lst[i] = ['',0]
		return lst

def findCompleted(workers):
	completed = []
	for x in workers:
		if x[1] == 0:
			completed.append(x[0])
	return completed
	
def isIdle(workers):
	for x in workers:
		if x[1] == 0:
			return True
	return False
	
def completeRemaining(workers):
	maxi = 0
	for x in workers:
		if x[1] > maxi:
			maxi = x[1]
	return maxi

while stepsLeft:
	if isIdle(workers):
		newComplete = findCompleted(workers)
		for x in newComplete:
			completed.append(x)

		nextSteps = getReady(completed, stepsLeft)
		while isIdle(workers) and nextSteps:
			workers = assignWorker(workers, nextSteps[0])
			stepsLeft.remove(nextSteps[0])
			nextSteps = nextSteps[1:]
		if isIdle(workers):
			workers = assignWorker(workers, '')
				
	workers = oneSecond(workers)
	elapsed += 1
	print(workers)

elapsed += completeRemaining(workers)

print("".join(completed))
print(elapsed)
