'''Quick Check: Exceptions as classes
If MyError inherits from Exception, what is the difference between except
Exception as e and except MyError as e?'''

# The first catches any exception that inherits from Exception (most of them), 
# whereas the second catches only MyError exceptions.