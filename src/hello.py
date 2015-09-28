# This is a commented line, notice that it starts with a '#'.
# The python interpretter will ignore anything after a '#'

""" The Python interpretter will also ignore anying contained in 
triple quotes, even if it spans multiple lines. We can use these 
'comments' to tell other people how to use our code. Well written code
has comments to help others understand our algorithms."""

print("Hello World!")
# print() is a 'function' which is used to write things to the screen!

# We can assign values to variables using an 'assignment operator'!
my_variable = "Acton!"
# The '=' tells python to store 'Acton!' to the variable 'my_variable'

# From now on, I can use 'my_variable' to express the value 'Acton!'

# For example
print("Hello", my_variable)
# will print 'Hello Acton!'

""" In the lines above the variable 'my_variable' is holding a word, 
which we will refer to as a 'string of characters' or a 'string' for 
short. We have to enclose these 'strings' in quotations so that Python
knows that they all belong together. If we don't enclose the string in 
quotes then python will think we are trying to access a variable! """

# Variables can be 'reassigned', allowing them to take a new value
my_variable = "Hackrrspace!"
# the old value, 'Acton!', is now gone!

print("Hello", my_variable)
# will print 'Hello Hackrrspace!'

""" We can also collect a variable from outside our program by asking 
the 'user' a question"""

first_name = input("Type your first name (then press enter): ")

""" 'input' is another function, this one allows Python to read a string 
from the command line. In the line above this input is stored in the 
variable 'first_name'. """

print("Hello", first_name, "!")

"""
***** TASK *****
Modify this program so that it asks the user a few other questions. 
Find out the user's last name, and age, then print it to the screen so 
that it looks like this:

Hello Paul Stiverson, you are 32 years old!

Go!
"""

"""
***** TASK *****
In another file, write a program that will print a tic-tac-toe board to 
the screen using hyphens (-), plus signs (+), and pipes (|).

call this file 'tic-tac-toe.py'

It should look like this:

   |   |
---+---+---
   |   |
---+---+---
   |   |

Go!
"""
