'''
Try this: Create a dictionary
Write the code to ask the user for three names and three ages. After the names and ages
are entered, ask the user for one of the names, and print the correct age.
'''

nameage_dict = {}
for i in range(0,3):
	name = str(input("Enter your name: "))
	age = int(input("Enter your age: "))
	nameage_dict[name] = age

who = input("Whose age do you want? ")

if who in nameage_dict:
	print("{}'s age is: ".format(who))
else:
	print("Sorry, there is no {} in the records".format(who))
