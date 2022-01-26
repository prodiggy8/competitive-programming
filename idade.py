# Camila's age, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/idade/
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c: # A maior
	if b <= c and b <= a: # B menor
		print(c)
	else:
		print(b) # C menor
elif b >= a and b >=c: # B maior
	if a <= c and a <= b: # A menor
		print(c)
	else:
		print(a) # C menor
else:
	if a <= c and a <= b: # A menor
		print(b)
	else:
		print(a)