# Skyscrapper, 2017 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/pu/2017/f3/arranhaceu/

na, ne = [int(i) for i in input().split()]
people = [int(i) for i in input().split()]

for i in range(ne):
	event = [str(i) for i in input().split()]

	if event[0] == '0':
		people[int(event[1]) - 1] = int(event[2])

	else:
		s = 0
		for j in range(int(event[1])):
			s += people[j]
		print(s)


