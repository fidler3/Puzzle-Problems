def UniqueString(str):
	a = sorted(str)
	for i, letter in enumerate(a):
		if i == len(a)-1:
			return True;
		elif letter == a[i+1]:
			return False

print(UniqueString("lollipop"))

print(UniqueString("join"))

def isPermutation(stringa, stringb):
	stringa = ''.join(sorted(stringa))
	stringb = ''.join(sorted(stringb))
	return (stringa == stringb)

print(isPermutation("cinema", "iceman"))
print(isPermutation("William", "Jennifer"))
print(isPermutation("Cinema", "iceman"))


def URLify(str1, lenstr):
	chars = list(str1)
	for i, c in enumerate(chars):
		if c == " ":
			chars[i] = "%20"
	return ''.join(chars)

word = "benny and the jets"

print(URLify(word, len(word)))

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

def oneaway(str1, str2):
	a = list(str1)
	b = list(str2)
	if len(a)+1==len(b):
		i = 0
		j = 0
		while(i<len(a) and j<len(b)):
		 	if a[i] != b[j]:
		 		if i != j:
		 			return False
		 		j+=1
		 	else:
		 		i+=1
		 		j+=1
		return True

	elif len(a)-1==len(b): 
		i = 0
		j = 0
		while(i<len(a) and j<len(b)):
		 	if a[i] != b[j]:
		 		if i != j:
		 			return False
		 		i+=1
		 	else:
		 		i+=1
		 		j+=1
		return True
	elif len(a) == len(b):
		count = 0

		for i, letter in enumerate(a):
			if letter != b[i]:
				count +=1
				if count == 2:
					return False
		return True 
	else:
		return False
		
print(oneaway("pale","ple"))
print(oneaway("pales", "pale"))
print(oneaway("pale", "bale"))
print(oneaway("pale", "bake"))