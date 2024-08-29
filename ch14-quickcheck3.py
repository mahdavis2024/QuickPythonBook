'''Quick Check: Context managers
Assume that you’re using a context manager in a script that reads and/or writes several
files. Which of the following approaches do you think would be best?

A) Put the entire script in a block managed by a with statement.
B) Use one with statement for all file reads and another for all file writes.
C) Use a with statement each time you read a file or write a file (for each line, for example).
D) Use a with statement for each file that you read or write.'''

# The best approach would be D) Use a with statement for each file that you read or write.
# Using a with statement for each file ensures that each file is properly opened and closed, 
# which is crucial for resource management. 
# This approach helps prevent resource leaks 
# and ensures that files are closed as soon as their operations are complete, 
# even if an error occurs during the process