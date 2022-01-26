# Time, 2021 Brazilian Informatics Olympiad
# Available @ https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/tempo/
n = int(input())
events = []
final  = []

for i in range(n): # Adjacent list
	events.append([str(i) for i in input().split(' ')])

for i in range(n): # Calculate every friend
	if events[i][0] == 'R':
		current = events[i][1]
		time = 0
		last = 0

		for j in range(i + 1, n): # Search for the answer
			if last:
				if events[j][0] == 'E' and events[j][1] == current:
					final.append([current, time])
					break
				else:
					last = 0
					continue;
			else:
				if events[j][0] == 'E' and events[j][1] == current:
					final.append([current, time + 1])
					break
				elif j == (n - 1):
					final.append([current, -1])
					break
				elif events[j][0] == 'T':
					time += int(events[j][1])
					last = 1
					continue
				else:
					time += 1
					continue

names = []
times = []
passe = []

for i in range(len(final)):
	if final[i][0] not in passe:
		names.append(final[i][0])
		times.append(final[i][1])
		passe.append(final[i][0])
	else:
		index_passed = names.index(final[i][0])
		if final[i][1] == -1:
			times[index_passed] = -1
		else:
			times[index_passed] += final[i][1]
final = []
for i in range(len(times)):
	final.append([names[i], times[i]])

final.sort(key=lambda x: x[0])
for i in range(len(final)):
	print(final[i][0],final[i][1])
				