from time import time
start = time()
maximum = 1000000
smallMax = maximum - 2
numbers = []

for i in range(2,maximum):
	numbers.append(0)
numbers[0] = -1
numbers[1] = -1

for n in range(2, smallMax):
	fractMax = smallMax/n - 2
#	print n
#	print numbers[n]
	if numbers[n] == 0:
		for x in range(2,fractMax):
			composite = n*x
			while composite < smallMax:
#				print composite
				if numbers[composite] == 0:
					numbers[composite] = -1
					break
				else: break
		
primes = [k for k,v in enumerate(numbers) if k > 1 and v == 0]
print primes
print time() - start