""" Welcome lvl1 programmer, in the last file you proved your worthiness
to move forward. In this file we will explore how we can make our 
programs more tolerant of all the things that can go wrong in a program.
"""

print("Have you ever noticed how Python freaks out when you don't give it the \
type of data it expects?")
answer = eval(input("yes/no ? "))

""" Oops I miswrote the line above to make Python look for a number but
I made you think you should enter letters. The resulting error is called 
a runtime error or an 'exception'. Specifically this exception is 
called a 'NameError'. Before running this program again you should 
comment out that line! 

These sorts of errors can creep in every time we ask the user for input
or from bugs in our own code. If we want our programs to be robust then
they will need to be able to deal with these types of errors.

Fortunately, Python has a built in way of handling these errors, it is 
called a 'try-except block'. Below we will ask the user to enter a 
number, but we will warn Python to expect an error.
"""

try:
    a_number = eval(input("enter a number? "))
    # I can also tell Python what sort of error to look for:
except NameError:
    print("I said a number!! I'm going to default to 5")
    a_number = 5
    # and I can tell Python what to do if no error was found
else:
    print("Good user!")

""" There are other errors we might want to watch out for as well. 
Luckily Python can handle multiple errors with ease!
"""

try:
    another_number = eval(input("enter another number to divide by: "))
    quotient = a_number / another_number
except NameError:
    print("I said a number!!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero. What are you trying to pull here!?")
else:
    print("Good user, the quotient is", quotient);

""" Python knows about many more types of exceptions. A long list can be 
found in the documentation: 
    https://docs.python.org/3.4/library/exceptions.html

In addition to the built-in exceptions we can also teach Python new 
ones to handle specific issues that arise in our programs. 
We will do this later.
"""

"""
***** TASK *****
In another file write a program that will ask the user to input a 
number, keep asking until they actually enter a number. 
Do nothing with that number.

call this file 'asker_not_doer.py'

Go!
"""

"""
***** TASK *****
Modify your 'advanced_tic_tac_toe.py' to ensure that the user enters a 
number before attempting to print the tic-tac-toe board.

Go!
"""