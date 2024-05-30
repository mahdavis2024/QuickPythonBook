'''
Try this: Comprehensions
What list comprehension would you use to process the list x so that all negative values
are removed?
'''
x = [1, 3, 5, 0, -1, 3, -2]
x = [item for item in x if item > -1]
print(x)
'''
Create a generator that returns only odd numbers from 1 to 100. 
(Hint: A number is odd if there is a remainder if divided by 2; use % 2 to get the remainder of division by 2.)
'''
odd = (i for i in range(1, 100) if i % 2 > 0)
#test
for o in odd:
	print(o)
'''
Write the code to create a dictionary of the numbers and their cubes from 11 through 15.
'''
xcubes = {x : x*x for x in range(11,16)}
print(xcubes)