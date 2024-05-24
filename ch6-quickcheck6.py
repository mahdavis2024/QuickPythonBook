'''
Quick Check: the format() method
What will be in x when the following snippets of code are executed?:
x = "{1:{0}}".format(3, 4)
x = "{0:$>5}".format(3)
x = "{a:{b}}".format(a=1, b=5)
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
'''
x = "{1:{0}}".format(3, 4)
print(x)
x = "{0:$>5}".format(3)
print(x)
x = "{a:{b}}".format(a=1, b=5)
print(x)
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
print(x)

'''
  4
$$$$3
    1
    1:3$$$$
'''