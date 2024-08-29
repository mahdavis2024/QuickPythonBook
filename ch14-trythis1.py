'''
Try this: Catching exceptions
Write code that gets two numbers from the user and divides the first number by the
second. Check for and catch the exception that occurs if the second number is zero
(ZeroDivisionError)'''

x = int(input('Enter the numerator : '))
y = int(input('Enter the denominator: '))
# x,y = 5,0
try:
	z = x / y
except ZeroDivisionError as er:
	print(er, '"The denominator cannot be zero."')
	y = input('Enter another denominator: ')

print('The quotient: ', z)