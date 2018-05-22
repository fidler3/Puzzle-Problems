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

