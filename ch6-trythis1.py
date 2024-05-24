'''
Try this: String operations
Suppose that you have a list of strings in which some (but not necessarily all)
 of the strings begin and end with the double quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
What code would you use on each element to remove just the double quotes?
What code could you use to find the position of the last p in Mississippi? 
When you’ve found that position, what code would you use to remove just that letter?
'''
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']

y = []
for i in x:
	n = i.strip('"')
	y.append(n)
x = y
print(x)	

#####################
m = "Mississippi"
n = []
for i in m:
	n.append(i)
del(n[m.rfind("p")])
l =''.join(n)
print(l)
