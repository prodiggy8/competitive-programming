# Dangerous fissure, 2020 Brazlian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/fissura/

n, f = [int(i) for i in input().split(' ')]
mapa = []

for i in range(0, n):
	mapa.append([])
	temp = input()
	for j in range(0, n):
		mapa[i].append(int(temp[j]))

start = False
for i in range(0, n):
	for j in range(0, n):
		if start == False:
			if f >= mapa[i][j]:
				mapa[i][j] = "*"
				start = "True"
		if i > 0:
			if mapa[i - 1][j] == "*":
				if f >= mapa[i][j]:
					mapa[i][j] = "*"
					continue
		if j > 0:
			if mapa[i][j - 1] == "*":
				if f >= int(mapa[i][j]):
					mapa[i][j] = "*"
					continue
		if i < n - 1:
			if mapa[i + 1][j] == "*":
				if f >= mapa[i][j]:
					mapa[i][j] = "*"
					continue
		if j < n - 1:
			if mapa[i][j + 1] == "*":
				if f >= mapa[i][j]:
					mapa[i][j] = "*"
					continue

for i in range(0, n):
	temp = ''.join([str(int) for int in mapa[i]])
	print(temp)


