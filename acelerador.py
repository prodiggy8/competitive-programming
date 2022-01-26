# Particle Accelerator, 2020 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/passadas/OBI2020/fase1/programacao-a/

n = int(input())
n = n - 5
m = n % 8

if m == 2 or m == 3:
	print(m)
else:
	print(1)