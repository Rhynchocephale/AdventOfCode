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

completed = []
ready = set()

def getReady(completed, stepsLefts):
	ready_tmp = set([_ for _ in stepsLeft])
	for x in data:
		if not x[0] in completed:
			try:
				ready_tmp.remove(x[1])
			except KeyError:
				pass
	return sorted(list(ready_tmp))
			
while stepsLeft:
	nextStep = getReady(completed, stepsLeft)[0]
	completed.append(nextStep)
	stepsLeft.remove(nextStep)
	
print("".join(completed))
