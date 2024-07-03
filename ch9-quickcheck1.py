'''
Quick Check: Functions and parameters
How would you write a function that could take any number of unnamed arguments
and print their values out in reverse order?
'''
# if reverse order mean descending order:
def reverser(*a):
    my_list = [*a]
    my_list.sort(reverse = True)
    for j in my_list:
        print(j)

reverser(8,5,4,1,3,9,7)
# if reverse means LIFO:

def lifo(*args):
    my_list = [*args]
    my_list.reverse()
    for i in my_list:
        print(i)

lifo('i','c','a','n')        
   

'''
What do you need to do to create a procedure or void function—that is, a function with
no return value?
'''
# There would not be a return statement at the end of the function.
# Or there would not be anything in front of the return statement.
# The funtion can do one of the following to still be productive:
## The procedure might make some changanes to a mutable type, which would hold outside the function.
## Or it can print something in terminal.
## Or it may save a file locally or push a code ...


'''What happens if you capture the return value of a function with a variable?'''
# it is possible to use that variable as any other variable then.





