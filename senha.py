# Password, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/senha/

def pwd(password, i):
	for j in range(k):
		temp = []
		for f in range(n):
			temp.append(password[f])
	
		temp[index[i]] = words[i][j]
		
		if i == (m - 1):
			possi.append(temp)
		else:
			pwd(temp, i + 1)
	return

n, m, k = [int(i) for i in input().split()]

senha = list(str(input()))
words = []
possi = []
index = []

for i in range(m): #Palavras
	temp0 = list(str(input()))
	words.append(temp0)

p = int(input())

for i in range(n): #Indices das letras desconhecidas
	if senha[i] == '#':
		index.append(i)

pwd(senha, 0)
possi.sort()
print(''.join(possi[p - 1]))
