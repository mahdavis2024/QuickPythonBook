'''
Try this: Decorators
How would you modify the code for the decorator function to remove unneeded
messages and enclose the return value of the wrapped function in "<html>" and "
</html>", so that myfunction ("hello") would return "<html>hello<html>"?
'''

def decorate(func):
	def wrapper_func(*args):
		return func('<html>{}</html>'.format(*args))
	return wrapper_func 
##
@decorate 
def myfunction(parameter):
	print(parameter)


myfunction("meu meu")
