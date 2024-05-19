'''
Try this: List slices and indexes
Using what you know about the len() function and list slices, how would you combine
the two to get the second half of a list when you don’t know what size it is? 
Experiment in the Python shell to confirm that your solution works.
'''

x = [00, 11, 22, 33, 44, 55, 66, 77, 88]
y = x[len(x)//2:]
print(y)