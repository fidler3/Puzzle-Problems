def loopdetection(node):
	if node == null:
		return False
	if node.next != node:
		return False
	else:
		a = node
		b = node.next.next;
		while a != null or b != null:
			if a == b:
				return True
			else
				a = a.next
				b = b.next.next

		return False 
