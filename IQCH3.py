You could implent a array and each index of an array is 
a linked list. Everytime you push something onto the stack
(stack 0, stack 1 stack 2) you would insert the data into
a node, and insert that node as the new head. The size of 
the array would be the amount of stacks you would want. Popping
and pushing would both be constant time.

def stackObject():
	min