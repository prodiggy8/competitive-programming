# Olympiad Shirts, 2020 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/camisetas/
n = int(input())
pn = 0
mn = 0

for i in input().split(' '):
	if int(i) == 1:
		pn += 1
	else:
		mn += 1

p = int(input())
m = int(input())

if (pn == p) and (mn == m):
	print('S')
else:
	print('N')

