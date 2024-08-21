'''
Quick Check: Manipulating paths
How would you use the os module’s functions to take a path to a file called test.log
and create a new file path in the same directory for a file called test.log.old? How
would you do the same thing using the pathlib module?
What path would you get if you created a pathlib Path object from os .pardir? Try it
and find out.
'''
import os
old_path = os.path.abspath('test.log')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)

import pathlib
path = pathlib.Path('test.log')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)