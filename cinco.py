# Five, 2018 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/pu/2018/f3/cinco/

n = int(input())
number = [int(i) for i in input().split()]

if number[n - 1] not in [0, 5]:
	for i in range(n):
		if number[i] in [0, 5]:
			if number[n - 1] > number[i]:
				temp = number[i]
				number[i] = number[n - 1]
				number[n - 1] = temp
				for j in number: print(j, end=" ")
				exit()

print('-1')