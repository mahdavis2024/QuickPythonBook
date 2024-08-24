'''
Quick Check
What is the significance of adding a "b" to the file open mode string, as in
open("file", "wb")?'''
# it wirtes to the file in byte mode.

'''
Suppose that you want to open a file named myfile.txt and write additional data on
the end of it. What command would you use to open myfile.txt? What command
would you use to reopen the file to read from the beginning?'''
with open('myfile', 'a') as mine:
	mine.write('this is the added content')

with open('myfile') as mine:
	for line in mine.readline():
		pass

