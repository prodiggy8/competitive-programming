# Calculation, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/calculo/
s = int(input())
a = int(input())
b = int(input())
numbers = 0

for i in range(a, b + 1):
	total = 0
	temp = str(i)
	for j in range(len(temp)):
		total += int(temp[j])

	if total == s:
		numbers += 1

print(numbers)