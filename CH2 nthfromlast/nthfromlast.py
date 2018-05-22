
def nthfromlast(node, n):
	fup = node
	sup = node
	count = 0

	while fup != None:

		if count == n:
			fup = fup.next
			sup = sup.next
		else:
			fup = fup.next
			count++

	sup.next = sup.next.next

