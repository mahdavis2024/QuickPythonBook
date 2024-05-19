'''
Quick Check: List Operations
What would be the result of len([[1,2]] * 3)?
What are two differences between using the in operator and a list’s index() method?
Which of the following will raise an exception?: min(["a", "b", "c"]); max([1, 2, "three"]); [1, 2, 3].count("one")
'''

x = [[1,2]] * 3
print(x)
print(len(x))

y = [9, 8, 7, 0, 1, 7]
print(2 in y)				#returns only boolean, no more information of the position
print(8 in y)
print(y.index(7))			#returns the position of only the first occurance
#print(y.index(2))			#returns Traceback ValueError: 2 is not in list


print(min(["a", "b", "c"]))

#print(max([1, 2, "three"]))       #TypeError: '>' not supported between instances of 'str' and 'int'

print([1, 2, 3].count("one"))




