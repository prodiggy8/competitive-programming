# Integers' marriage, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/static/extras/obi2021/provas/ProvaOBI2021_f3p2.pdf

a = [int(i) for i in list(input())]
b = [int(i) for i in list(input())]

if len(a) < len(b):
	for i in range(len(b) - len(a)):
		a.insert(0, 0)
elif len(b) < len(a):
	for i in range(len(a) - len(b)):
		b.insert(0, 0)

for i in range(len(a)):
	if a[i] < b[i]:
		a[i] = -1
	elif b[i] < a[i]:
		b[i] = -1
	else:
		continue

try:
	a = [x for x in a if x != -1]
	b = [x for x in b if x != -1]
except ValueError:
	pass

if not a:
	a = -1
else:
	a = [str(x) for x in a]
	a = int(''.join(a))

if not b:
	b = -1
else:
	b = [str(x) for x in b]
	b = int(''.join(b))

if b < a:
	print(b, a)
else:
	print(a, b)