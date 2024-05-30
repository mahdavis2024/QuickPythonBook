'''
Try this: Looping and if statements
Suppose that you have a list x = [1, 3, 5, 0, -1, 3, -2], and you need to
remove all negative numbers from that list. Write the code to do this.
'''
x = [1, 3, 5, 0, -1, 3, -2]
j = 0
for i in range(len(x)):
	if x[i - j] < 0:
	   del(x[i - j])
	   j += 1
print(x)

'''
How would you count the total number of negative numbers in a list 
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]?
'''
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
tot = 0
for i in range(len(y)):
	for j in range(len(y[i])):
		if y[i][j] < 0:
			tot = tot + y[i][j]
print('total of negetives: ', tot)

'''
What code would you use to print very low if the value of x is below -5, low if it’s
from -5 up to 0, neutral if it’s equal to 0, high if it’s greater than 0 up to 5, and very
high if it’s greater than 5?
'''
def ranking(x):
	if x < -5:
		print('x is very low')
	elif x < 0:
		print('x is low')
	elif x == 0:
		print('x is neutral')
	elif x < 5:
		print('x is high')
	else:
		print('x is very high')
# test
for i in range(-7 , 7):
	print(i)
	ranking(i)
