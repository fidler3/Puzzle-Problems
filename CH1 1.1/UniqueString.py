def UniqueString(str):
	a = sorted(str)
	for i, letter in enumerate(a):
		if i == len(a)-1:
			return True;
		elif letter == a[i+1]:
			return False

print(UniqueString("lollipop"))

print(UniqueString("join"))

