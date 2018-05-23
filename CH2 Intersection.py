def intersection(node a, node b):
	alist = []
	atemp = a
	while a != null:
		alist.append(a)

	while b != null:
		if alist.contains(b):
			return True
	return False
