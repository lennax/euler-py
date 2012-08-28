argument = 100
factorial = 1

for n in range(argument,0,-1):
	factorial = factorial * n

#print factorial

#below stolen from 16
total = 0

factorial = str(factorial)
for n in range(0,len(factorial)):
	digit = int(factorial[n])
	total += digit
	
print total