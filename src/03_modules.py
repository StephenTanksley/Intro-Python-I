"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print("first arg: \n", sys.argv[0])
# print("second arg: ", sys.argv[1])

# Print out the OS platform you're using:
# YOUR CODE HERE

print("os platform: \n", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE

print("python version: \n", sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("process id: \n", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("working directory: \n", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("machine's login name: \n", os.getlogin())
