# Rectangle, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/retangulo/

n = int(input())
tree = [int(i) for i in input().split(' ')]

soma = sum(tree)

for i in range(n):
	temp = 0

	for j in range(n):
		temp += tree[(i + j - 1) % n]

		if (temp > float(soma / 2)):
			break

		elif temp == float(soma / 2):
			temp2 = 0

			for k in range(n):
				temp2 += tree[(i + k) % n]

				if temp2 == temp:
					print('S')
					exit(0)

				if (temp2 > float(soma / 2)):
					break

print('N')



