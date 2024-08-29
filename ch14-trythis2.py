'''Try this: The assert statement
Write a simple program that gets a number from the user and then uses the assert
statement to raise an exception if the number is zero. Test to make sure that the
assert statement fires; then turn it off, 
using one of the methods mentioned in this section.'''

x = int(input('Enter a number: '))

print(__debug__)

assert x != 0, 'the number is zero'
print('entered:', x)