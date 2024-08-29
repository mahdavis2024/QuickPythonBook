'''Quick Check: Exceptions
Do Python exceptions force a program to halt?
Suppose that you want accessing a dictionary x to always return None if a key doesn’t
exist in the dictionary (that is, if a KeyError exception is raised). What code would you
use?
'''
# not if the exception is safely handled and else and finally clause used.

def check_dict(dict,akey):
	try:
		val = dict[akey]
	except KeyError as e:
		val = None
