maximum = 1000
total = 0

for i in range(1,maximum):
	increment = pow(i, i)
#	print increment
	total += increment
	
#does not give last 10 digits, gives whole number
print total

#revised to grab last 10 digits; more or less copied from euler13
total = str(total)
tenTotal = ""
for x in range(10,0,-1):
	tenTotal += total[-x]

print tenTotal