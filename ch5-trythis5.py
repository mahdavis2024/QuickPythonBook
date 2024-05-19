'''
Try this: List copies
Suppose that you have the following list: x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
What code could you use to get a copy y of that list in which you could change the
elements without the side effect of changing the contents of x?
'''
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


shallow = x[:]
print('shallow    ', shallow)

import copy
deep = copy.deepcopy(x)

print('deep    ', deep)

del deep[1][1]
print('deep after del    ', deep)
print('x after deep del     ', x)

del shallow[2][2]
print('shallow after del     ', shallow)
print('x after shallow del     ', x)