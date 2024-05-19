'''
Quick Check: Tuples
Explain why the following operations aren’t legal for the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?
'''

x = (1, 2, 3, 4)
x.append(1) 		#Traceback	 AttributeError: 'tuple' object has no attribute 'append'
x[1] = "hello"		#Traceback	 TypeError: 'tuple' object does not support item assignment
del x[2]			#Traceback	 TypeError: 'tuple' object doesn't support item deletion

y = (3, 1, 4, 2)
print(sorted(y))        #[1, 2, 3, 4]
print(type(sorted(y)))	#<class 'list'>  turns the tuple to list then sorts
