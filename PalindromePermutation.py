def PalindromePermutation(str1):
	a = {}
	count = 0
	for letter in str1:
		if letter in a:				
			a[letter] += 1
		else:
			a[letter] = 1

	for key in a:
		if a[letter]%2 == 1:
			count += 1
		if count == 2:
			return False

	return True

print(PalindromePermutation("hitlame"))

