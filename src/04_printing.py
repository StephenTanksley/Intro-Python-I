"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# you use i to indicate integers, d for decimals, s for strings. Then you provide arguments using an argument mapping : % (x, y, z)
print("x is %i, y is %d, z is %s." % (x, y, z))

# Use the 'format' string method to print the same thing
# Need to use format() instead of how I have it here.
print("x is {}, y is {}, z is {}".format(x, y, z))

# Finally, print the same thing using an f-string

f_string = f"x is {x}, y is {y}, z is {z}"
print(f_string)
