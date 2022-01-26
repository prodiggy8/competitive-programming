# Square and cube, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/static/extras/obi2021/provas/ProvaOBI2021_f3p2.pdf

squarecube = [1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441, 1000000, 1771561, 2985984, 4826809, 7529536, 11390625, 16777216, 24137569, 
			34012224, 47045881, 64000000, 85766121] # all 21 square-cube numbers up to 100,000,000
a = int(input())
b = int(input())
counts = 0

for i in squarecube:
	if i >= a and i <= b:
		counts += 1

print(counts)