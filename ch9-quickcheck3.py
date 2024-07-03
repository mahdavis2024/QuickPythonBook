'''
Quick Check: Generator functions
What would you need to modify in the previous code for the function four()to make it
work for any number? 
What would you need to add to allow the starting point to also be
set?
'''

def any_number(starts, any):
	x = starts
	while x < any:
		print("in generator, x =", x)
		yield x 
		x += 1


for _ in any_number(5, 9):
	print(_)
