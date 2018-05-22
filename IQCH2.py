def remove_duplicates():
	node = node
	check = []
	nodebefore = None

	while node != None:
		if node.item in check:
			nodebefore.next = node.next
		else:
			check.append(node.item)

		previous = node
		node = node.next

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

def deletemiddle(node):
	by2 = node
	by1 = node
	first = True
	while by2 != None:
		if first:
			first = False 
			by2 = by2.next
			if(by2 == None):
				by1.next = by1.next.next
			else:
				by2 = by2.next
		else:
			by2 = by2.next
			if(by2 == None):
				by1.next = by1.next.next
			else:
				by2 = by2.next
				by1 = by1.next
	by1.next = by1.next.next

