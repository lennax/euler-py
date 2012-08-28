haystack = str(pow(2,1000))
total = 0

for n in range(0,len(haystack)):
	digit = int(haystack[n])
	total += digit
	
print total
	