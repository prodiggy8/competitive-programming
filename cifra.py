# Nlogonia Cipher, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
v = ['a', 'e', 'i', 'o', 'u']

n = str(input())
f = []

for i in range(len(n)):
	if n[i] in v:
		f.append(n[i]) # vowel
		continue
	else:
		f.append(n[i]) # consonant
		
		index = a.index(n[i])

		if index <= 2: # next consonant
			f.append('a')
		elif index > 2 and index <= 6:
			f.append('e')
		elif index > 6 and index <= 11:
			f.append('i')
		elif index > 11 and index <= 17:
			f.append('o')
		else:
			f.append('u')

		if index != (len(a) - 1): # next consonant except for Z
			for j in range(index + 1, len(a)):
				if a[j] not in v:
					f.append(a[j])
					break
		else:
			f.append(a[index])
print(''.join(f))