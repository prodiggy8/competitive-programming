# Pandemic, 2020 Brazilian Informatics Olympiad 2020
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/pandemia/


n, d = [int(i) for i in input().split(' ')]
ni, di = [int(i) for i in input().split(' ')]

m = []

inf = [ni]
num = 1

for i in range(0, d):
	temp = []
	temp = [int (f) for f in input().split(' ')]
	m.append(temp)

for i in range(0, d):
	if (i >= di - 1):
		for j in range(1, m[i][0] + 1):
			if (m[i][j] not in inf):
				inf.append(m[i][j])
				num += 1
print(num)