# Three for Two, 2020 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/3por2/

n = int(input())
p = []
j = 1
total = 0

for i in range(0, n):
	p.append(int(input()))
p.sort()

x = 0
if not (n % 3):
	x = n / 3
else:
	x = n % 3
for i in range(0, (n % 3)):
	total += p[n - j]
	j += 1
	p.pop()

	total += p[n - j]
	j += 1
	p.pop()

	p.pop(0)

total += sum(p)
print(total)