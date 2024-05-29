'''
Try this: Using dictionaries
Suppose that you’re writing a program that works like a spreadsheet. 
How might you use a dictionary to store the contents of a sheet? 
Write some sample code to both store a value and retrieve a value in a particular cell. 
What might be some drawbacks to this approach?
'''

spreadsheet = {}

x = input('enter x index of cell: ')
y = input('enter x index of cell: ')

cell_content = spreadsheet.get((x, y), input('enter content for this cell: '))
