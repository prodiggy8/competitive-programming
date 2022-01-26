# Zero to cancel, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/zero/

n = int(input())
x = []

for i in range(n):
	t = int(input())
	if (t == 0):
		x.pop()
	else:
		x.append(t)
print(sum(x))