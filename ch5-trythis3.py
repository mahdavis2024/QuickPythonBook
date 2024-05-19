'''
Try this: Sorting lists
Suppose that you have a list in which each element is in turn a list: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]. 
If you wanted to sort this list by the second element in each list
so that the result would be [[4, 0, 1], [2, 1, 3], [1, 2, 3]], what function
would you write to pass as the key value to the sort() method?
'''

def second_item(in_list):
	return in_list[1]

x = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
x.sort(key = second_item)
print(x)