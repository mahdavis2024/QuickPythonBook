# working with os

import os
os.getcwd()  # current working directory
os.curdir # constant, returns whatever string your system happens to use as the same directory indicator . or ..
os.listdir(os.curdir) # returns a list of filenames in the current working directory 
os.listdir() # appends it to the path for the current working directory
os.chdir(folder name) #  “Change directory” function, moves into that folder
os.name # constant returns the name of the Python module imported to handle the operating system: 'nt' for windows, 'posix' for linux
os.environ #All your environment variables and the values associated with them are available in a dictionary
os.rename('old name', 'new name') # To rename (move) a file or directory
os.remove() # Remove or delete a data file with 
os.rmdir() # To remove an empty directory 
os.mkdir() # create directory without any necessary intermediate directories
os.makedirs() # create directory with all necessary intermediate directories

os.path.join() # construct pathnames by componants
os.path.split() # returns a two-element tuple splitting the basename of a path
os.path.basename() # returns only the basename of the path
os.path.dirname() # returns the path up to but not including the last name
os.path.splitext() # returns a tuple with separated file extention 
os.path.commonprefix(path1, path2, ...) # finds the common prefix (if any) for a set of paths
os.path.expanduser() # expands username shortcuts in paths
os.path.expandvars() # expands environment variables
os.path.isdir(os.path.join(path, os.pardir, os.curdir)) # asks whether the parent of the parent of path is a directory

os.path.exists() # returns True if its argument is a path corresponding tosomething that exists in the filesystem
os.path.isfile() # returns True if and only if the path it’s given indicates a normal data file of some sort
os.path.isdir() # returns True if and only if its path argument indicates a directory
os.path.islink() # Linux and other UNIX operating
os.path.ismount() # Linux and other UNIX operating
os.path.samefile(path1, path2) # returns True if and only if the two path arguments point to the same file
os.path.isabs(path) # returns True if its argument is an absolute path
os.path.getsize(path) # returns the size of a pathname
os.path.getmtime(path) # returns the last modify time of a pathname
os.path.getatime(path) # returns last access time of a pathname

# working with pathlib
import pathlib
cur_path = pathlib.Path()
cur_path.cwd()

from pathlib import Path
cur_path = Path()
cur_path.joinpath()
a_path = WindowsPath('bin/utils/disktools')
a_path.parts # returns a tuple of all the components of a path
a_path.name # returns only the basename of the path
a_path.parent # returns the path up to but not including the last name
a_path.suffix # dotted extension notation used by most filesystems to indicate file type 
new_path = cur_path.joinpath('C:', 'my documents', 'tmp')
new_path.iterdir() # returns an iterator of paths
new_path.unlink() # Remove or delete a data file
new_path.mkdir(parents=True) # creates directory with any necessaryintermediate directories
new_path.rmdir() # To remove an empty directory