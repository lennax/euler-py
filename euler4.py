palindromes = []
product = 0

for first in range(999,99,-1):
	isPalindrome = 0
	for second in range(999,99,-1):
		product = first*second
		if str(product) == str(product)[::-1]:
			palindromes.append(product)

max = 0
for palindrome in palindromes:
	if palindrome>max: max = palindrome

print max