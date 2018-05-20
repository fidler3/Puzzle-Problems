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