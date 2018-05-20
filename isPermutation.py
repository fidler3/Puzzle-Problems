
def isPermutation(stringa, stringb):
	stringa = ''.join(sorted(stringa))
	stringb = ''.join(sorted(stringb))
	return (stringa == stringb)

print(isPermutation("cinema", "iceman"))
print(isPermutation("William", "Jennifer"))
print(isPermutation("Cinema", "iceman"))


