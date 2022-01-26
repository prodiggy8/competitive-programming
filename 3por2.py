# Three for Two, 2020 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/3por2/

n = int(input())
price = []
s = 0

for i in range(0, n):
	price.append(int(input()))

price.sort()
high = n % 3

for i in range(0, high):
	price[n - i - 1] = 0

for i in range(0, n):
	s += price[i];

print(s)
	
