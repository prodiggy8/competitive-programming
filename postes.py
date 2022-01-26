# Poles, 2017 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/static/extras/obi2017/provas/ProvaOBI2017_f3p2.pdf

n = int(input())
p = [int(i) for i in input().split(' ')]

s = 0
c = 0


for i in range(n):
	print(p[i])
	if p[i] < 50:
		s += 1
	elif p[i] >= 50 and p[i] < 85:
		c += 1
	else:
		continue

print(f'{s} {c}')

