'''
Try this: List operations
If you have a list x, write the code to safely remove an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list more than once.
'''

def remove_if_is(x, item):
	if item in x:
		x.remove(item)
		return x
	else:
		return 'item not in the list'

def remove_first_one(x, item):
	if x.count(item) > 1:
		x.remove(item)
		return x
	else:
		return 'item less then twice in list'

y = [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

print(remove_if_is(y, 0))
print(remove_if_is(y, 7))
print(remove_first_one(y, 2))
print(remove_first_one(y, 6))
