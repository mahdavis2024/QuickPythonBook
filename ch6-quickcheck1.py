'''
Quick Check: split and join
How could you use split and join to change all the whitespace in string x to dashes,
such as changing "this is a test" to "this—is—a—test""?
'''
x = "this is a test"

x = '—'.join(x.split())

print(x)

