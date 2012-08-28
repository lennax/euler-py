from time import time
from math import sqrt
start = time()
arg = 600851475143
maximum = int(sqrt(arg))
smallMax = maximum - 2
numbers = []

for i in range(2,maximum):
	numbers.append(0)
numbers[0] = -1
numbers[1] = -1

for n in range(2, smallMax):
#	print n
#	print numbers[n]
	if numbers[n] == 0:
		composite = n+n
		while composite < smallMax:
#			print composite
			numbers[composite] = -1
			composite += n
		
primes = [k for k,v in enumerate(numbers) if k > 1 and v == 0]
print primes
print "primes"
print time() - start

factors = []

for prime in primes:
	if arg%prime == 0:
		factors.append(prime)

print factors
print "factor"
print time() - start