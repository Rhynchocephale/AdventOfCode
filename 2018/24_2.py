data = '''Immune System:
6638 units each with 2292 hit points (weak to radiation) with an attack that does 3 cold damage at initiative 18
3906 units each with 12319 hit points (immune to bludgeoning, cold, fire) with an attack that does 24 cold damage at initiative 14
2114 units each with 7254 hit points (immune to fire, radiation) with an attack that does 25 radiation damage at initiative 12
3157 units each with 1184 hit points (weak to bludgeoning) with an attack that does 3 cold damage at initiative 9
502 units each with 10367 hit points (weak to bludgeoning) with an attack that does 181 fire damage at initiative 13
1017 units each with 10287 hit points with an attack that does 88 cold damage at initiative 1
20 units each with 1333 hit points (immune to radiation, slashing; weak to bludgeoning) with an attack that does 508 fire damage at initiative 3
6263 units each with 6146 hit points with an attack that does 9 cold damage at initiative 2
5294 units each with 7781 hit points (weak to slashing; immune to fire) with an attack that does 12 slashing damage at initiative 5
807 units each with 4206 hit points (weak to slashing, bludgeoning) with an attack that does 44 fire damage at initiative 7

Infection:
1756 units each with 36633 hit points (immune to bludgeoning) with an attack that does 38 bludgeoning damage at initiative 17
1087 units each with 39027 hit points with an attack that does 64 slashing damage at initiative 10
2744 units each with 49920 hit points (weak to slashing) with an attack that does 30 fire damage at initiative 4
3849 units each with 21334 hit points (weak to bludgeoning) with an attack that does 10 cold damage at initiative 6
631 units each with 37995 hit points (weak to radiation) with an attack that does 85 fire damage at initiative 11
770 units each with 45051 hit points (weak to radiation, slashing) with an attack that does 114 radiation damage at initiative 20
1742 units each with 41529 hit points (immune to cold, fire) with an attack that does 46 bludgeoning damage at initiative 19
139 units each with 31968 hit points (weak to slashing) with an attack that does 458 cold damage at initiative 16
5191 units each with 28059 hit points with an attack that does 8 radiation damage at initiative 8
5797 units each with 33966 hit points with an attack that does 11 cold damage at initiative 15'''

#data = '''Immune System:
#17 units each with 5390 hit points (weak to radiation, bludgeoning) with  an attack that does 4507 fire damage at initiative 2
#989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

#Infection:
#801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
#4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'''

data = data.replace('Immune System:\n','').split('\nInfection:\n')

import copy, time

groups = []
ID = 0
for i in range(2):
	for group in data[i].split('\n'):
		if not group:
			continue
		units = int(group.split()[0])
		HP = int(group.split(' hit points')[0].split()[-1])
		initiative = int(group.split()[-1])
		damageType = group.split('damage')[0].split()[-1]
		damagePwr = int(group.split('damage')[0].split()[-2])
		
		weaknesses = []
		immunities = []
		try:
			elemental = group.split('(')[1].split(')')[0].split('; ')
			for x in elemental:
				if x.split()[0] == 'weak':
					weaknesses = x.replace('weak to ','').split(', ')
				if x.split()[0] == 'immune':
					immunities = x.replace('immune to ','').split(', ')
		except IndexError:
			pass

		newGroup = {
		'units': units,
		'HP': HP,
		'damageType': damageType,
		'damagePwr': damagePwr,
		'immunities': immunities,
		'weaknesses': weaknesses,
		'initiative': initiative,
		'ID': ID,
		'alive': True,
		'target': False,
		'side': 1-2*i
		}
		groups.append(newGroup)
		ID+=1

def orderGroupsByEffectivePower(groups):
	return sorted(groups, key=lambda x: effectivePower(x)*1000+x['initiative'], reverse=True)

def orderGroupsByInitiative(groups):
	return sorted(groups, key=lambda x: x['initiative'], reverse=True)

def effectivePower(group):
	return group['units']*group['damagePwr']

def listEnemies(group, groups):
	return [x for x in groups if x['side'] != group['side'] and x['alive']]

def damageCalc(attacking, defending):
	multiplier = 1
	if attacking['damageType'] in defending['immunities']:
		multiplier = 0
	elif attacking['damageType'] in defending['weaknesses']:
		multiplier = 2
		
	#print(attacking['damageType'], defending['weaknesses'], multiplier, multiplier*effectivePower(attacking))
	return multiplier*effectivePower(attacking)

def alreadySelected(group, groups):
	for group2 in groups:
		try:
			if group2['target']['ID'] == group['ID']:
				return True
		except TypeError:
			pass
	return False

def findTarget(group, groups):
	maxDmg = 0
	group['target'] = False
	target = ''
	for enemy in orderGroupsByEffectivePower(listEnemies(group, groups)):
		if not enemy['alive']:
			continue
		dmg = damageCalc(group, enemy)
		if dmg > maxDmg:
			if not alreadySelected(enemy, groups):
				target = enemy
				maxDmg = dmg
		elif dmg == maxDmg and target:
			if effectivePower(enemy) > effectivePower(target):
				target = enemy
			elif effectivePower(enemy) == effectivePower(target) and enemy['initiative'] > target['initiative']:
				target = enemy
	if maxDmg == 0:
		return groups
	group['target'] = target

	return groups

def attack(attacking, defending, groups):
	if not defending['alive'] or not attacking['alive']:
		return groups

	dmg = damageCalc(attacking, defending)
	defending['units'] -= dmg//defending['HP']
	if defending['units'] <= 0:
		defending['units'] = 0
		defending['alive'] = False
	attacking['target'] = False
	
	return groups

def isOver(groups):
	immune = listEnemies({'side': -1}, groups)
	infection = listEnemies({'side': 1}, groups)

	if len(immune) == 0:
		return -countUnits(infection)
	elif len(infection) == 0:
		return countUnits(immune)
	return False

def countUnits(groups):
	somme = 0
	for group in groups:
		if group['alive']:
			somme += group['units']
	return somme

oldGroups = copy.deepcopy(groups)
boost = -1
while True:
	boost += 1
	groups = copy.deepcopy(oldGroups)
	
	for group in groups:
		if group['side'] == 1:
			group['damagePwr'] += boost
	
	sumOfUnits = countUnits(groups)
	while True:
		groups = orderGroupsByEffectivePower(groups)
		#for x in groups:
		#	print(x['units'])
		
		previousSumOfUnits = sumOfUnits

		for group in groups:
			target = findTarget(group, groups)
		
		groups = orderGroupsByInitiative(groups)
		for group in groups:
			if group['target'] and group['alive']:
				groups = attack(group, group['target'], groups)
		if isOver(groups):
			print('boost:', boost)
			print('----')
			if isOver(groups)>0:
				print(isOver(groups))
				exit()
			break
		
		sumOfUnits = countUnits(groups)
		if sumOfUnits == previousSumOfUnits:
			print('boost:', boost)
			print('Stalemate')
			break
