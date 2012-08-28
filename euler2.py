prev = 0
curr = 1
total = 0
fib = 0

for k in range(0,35):
	fib = prev + curr
	
	if fib>=4000000:
		break;
	
	if fib%2 == 0:
		total = total+fib
		
	prev = curr
	curr = fib

print total
