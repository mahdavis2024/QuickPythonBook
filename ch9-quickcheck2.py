'''
Quick Check: Mutable function parameters
What would be the result of changing a list or dictionary that was passed into a function
as a parameter value?
Which operations would be likely to create changes that would be
visible outside the function? What steps might you take to minimize that risk?
'''
# The changes would hold outside the function as those are mutable data types.

# Operations like del, append, +, *, decreasing or increasing the list or dictionary by slice notation...

# It is possible to avoid modifying a list or dict by making a copy of them by .copy() and .deepcopy()
# and working with that copy. Though it would be wise to refrain from using mutable data types altogether.