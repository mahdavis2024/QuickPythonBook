'''
Quick Check: Modules
Suppose that you have a module called new_math that contains a function called
new_divide. What are the ways that you might import and then use that function?
What are the pros and cons of each method?
Suppose that the new_math module contains a function call _helper_math(). How
will the underscore character affect the way that _helper_math() is imported?
'''
# first
import new_math
new_math.new_divide()
'''prepending the module name is mandatory.
But the code is more readable and function names are safer to use 
and do not clash with other modules.'''

#second
from new_math import new_divide
new_divide()
'''imports a specific function, less keystrocks are needed for typing. 
do not bring upon other methods. function names might interfere with other names.'''

#third
from new_math import *
''' brings all the opjects inside the module.
this is risky as it does not indicated which functions blong to which module.
it faster in typing but more difficult for debugging.'''

import new_math
new_math._helper_math()
#or
from new_math import _helper_math
_helper_math()

''' _helper_math can be accessed using one of these two ways. but not the *.'''