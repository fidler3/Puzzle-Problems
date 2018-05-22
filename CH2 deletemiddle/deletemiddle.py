
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

