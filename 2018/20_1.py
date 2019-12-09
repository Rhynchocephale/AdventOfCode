data = '''^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'''

import re

while True:
	m = re.search('\([NSEW|]+\)', data)
	if not m:
		break
	part = sorted(data[m.span()[0]+1:m.span()[1]-1].split('|'), key=len)
	a = ''
	if part[0]:
		a = part[-1]
	data = data.replace(m.group(), a)

print(len(data)-2)
