from math import sqrt
triangle = 1
factors = 1
for n in range(2,1000):
	triangle += n
	factorList = []
	for k in range(2,triangle):
		if triangle%k == 0:
			factorList.append(k)
			factors += 1
			if len(factorList) >= 500:
				print triangle
print factorList