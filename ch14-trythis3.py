'''
Try this: Exceptions
What code would you use to create a custom ValueTooLarge exception and raise that
exception if the variable x is over 1000?'''

class ValueTooLarge(Exception):
	pass


def check_value_size(val):
		if val > 1000:
			raise ValueTooLarge('Value must be less than a thousand.')
