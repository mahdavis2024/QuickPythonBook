'''
Try this: Modifying lists
Suppose that you have a list 10 items long. How might you move the last three items
from the end of the list to the beginning, keeping them in the same order?
'''

x = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
print(x[-3:] + x[:-3])