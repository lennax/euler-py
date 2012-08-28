from time import time
from math import sqrt
start = time()
maximum = 100000000
numbers = []

for i in xrange(maximum):
	numbers.append(0)
numbers[0] = -1
numbers[1] = -1

stop = int(sqrt(maximum))
for n in xrange(2, stop):
#	print n
#	print numbers[n]
	if numbers[n] == 0:
		composite = n+n
		while composite < maximum:
#			print composite
			numbers[composite] = -1
			composite += n
		
primes = [k for k,v in enumerate(numbers) if k > 1 and v == 0]
#print primes
#total = sum(primes)
#print total
print time() - start