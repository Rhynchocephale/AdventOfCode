data = '''4 SRWZ, 3 ZGSFW, 1 HVJVQ, 1 RWDSX, 12 BDHX, 1 GDPKF, 23 WFPSM, 1 MPKC => 6 VCWNW
3 BXVJK, 3 WTPN => 4 GRQC
5 KWFD => 9 NMZND
1 DNZQ, 5 CDSP => 3 PFDBV
4 VSPSC, 34 MPKC, 9 DFNVL => 9 PZWSP
5 NTXHM => 9 DBKN
4 JNSP, 4 TCKR, 7 PZWSP => 7 DLHG
12 CNBS, 3 FNPC => 2 SRWZ
3 RWDSX, 4 NHSTB, 2 JNSP => 8 TCKR
24 PGHF, 1 NMZND => 3 RWDSX
1 DLHG => 9 QSVN
6 HVJVQ => 2 QSNCW
4 CHDTJ => 9 FDVNC
1 HBXF, 1 RWDSX => 7 BWSPN
2 ZGSFW, 1 KWFD => 8 JNSP
2 BWSPN, 7 GDPKF, 1 BXVJK => 6 FVQM
2 MHBH => 6 FNPC
2 WTPN, 15 GRQC => 3 ZGSFW
9 LXMLX => 6 CLZT
5 DFNVL, 1 KHCQ => 4 MHLBR
21 CNTFK, 3 XHST => 9 CHDTJ
1 CNTFK => 7 MHBH
1 GMQDW, 34 GDPKF, 2 ZDGPL, 1 HVJVQ, 13 QSVN, 1 QSNCW, 1 BXVJK => 2 SGLGN
1 BMVRK, 1 XHST => 8 XHLNT
23 CXKN => 1 BDKN
121 ORE => 9 XHST
4 NTXHM, 4 FNPC, 15 VCMVN => 8 MPKC
2 ZDGPL, 7 JNSP, 3 FJVMD => 4 GMQDW
1 LXMLX, 2 BWSPN => 2 DNZQ
6 WTPN => 9 KCMH
20 CDSP => 2 VSPSC
2 QSNCW, 1 BDHX, 3 HBXF, 8 PFDBV, 17 ZDGPL, 1 MHLBR, 9 ZGSFW => 8 FDWSG
2 VSFTG, 2 DLHG => 9 BDHX
174 ORE => 5 BMVRK
2 BMVRK => 2 KWFD
3 WTPN, 9 TVJPG => 9 CDSP
191 ORE => 2 CNTFK
9 FDVNC, 1 MHBH => 8 NTXHM
3 NHSTB, 2 BXVJK, 1 JNSP => 1 WFPSM
7 FJVMD => 9 CXKN
3 GDPKF, 10 QSNCW => 7 ZDGPL
7 LPXM, 11 VSPSC => 1 LXMLX
6 RWDSX, 2 NMZND, 1 MPKC => 1 KHCQ
6 RWDSX => 4 QMJK
15 MHBH, 28 DBKN, 12 CNBS => 4 PGHF
20 NMZND, 1 PGHF, 1 BXVJK => 2 LPXM
1 CDSP, 17 BXVJK => 5 NHSTB
12 HVJVQ => 3 VSFTG
2 PGHF, 3 VCMVN, 2 NHSTB => 1 DFNVL
5 FNPC => 9 HBXF
3 DPRL => 4 FJVMD
1 KWFD, 1 TVJPG => 8 VCMVN
1 FDWSG, 1 VCWNW, 4 BDKN, 14 FDVNC, 1 CLZT, 62 SGLGN, 5 QMJK, 26 ZDGPL, 60 KCMH, 32 FVQM, 15 SRWZ => 1 FUEL
3 XHLNT => 8 TVJPG
5 HBXF => 2 HVJVQ
3 CHDTJ, 15 KWFD => 9 WTPN
7 CNTFK => 7 CNBS
1 CNBS => 2 JPDF
5 JNSP => 8 DPRL
11 NTXHM => 8 GDPKF
10 JPDF => 9 BXVJK'''
data = data.split('\n')

from math import ceil

ore = 0
formulas = dict()
leftovers = dict()
for line in data:
	line = line.split(' => ')
	ingredients = line[0]
	result = line[1]
	ingredients = ingredients.split(', ')
	#7 A, 2 B => 1 C devient C: [1, 2, 7, A, 2, B]
	#qte resultat, nombre d'ingredients, qte + valeur pr chaque ingrédient.
	formula = [int(result.split(' ')[0]), len(ingredients)]
	for ingredient in ingredients:
		formula.append(int(ingredient.split(' ')[0]))
		formula.append(ingredient.split(' ')[1])
	formulas[result.split(' ')[1]] = formula

def getIngredients(name, qty):
	global leftovers, ore

	formula = formulas[name]
	if not name in leftovers:
		leftovers[name] = 0
	factor = ceil((qty-leftovers[name])/formula[0])
	leftovers[name] += factor*formula[0]-qty
	
	for i in range(formula[1]):
		if formula[3+2*i] == 'ORE':
			ore += factor*formula[2+2*i]
		else:
			getIngredients(formula[3+2*i], factor*formula[2+2*i])
	return

getIngredients('FUEL',1)
print(ore)
print(leftovers)