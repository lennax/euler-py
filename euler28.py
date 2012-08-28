total = 1
start = 1

for i in range(3,1002,2):
	for k in range(1,5):
		diagonal = start+k*(i-1)
		print diagonal
		total += diagonal
	start = diagonal

print total