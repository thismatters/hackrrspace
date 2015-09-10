""" Last time (in hello.py) we learned about variables and how they can
be set from inside the program and outside the program; all of
the variables in the last lesson were assigned strings. In this lesson
we will think about what other types of variables we can use. """


item_name = input('What do you want to buy? ')
# input() will accept a string input

item_price = eval(input('How much does it cost? $'))
""" When we are expecting a number we tell Python by wrapping the 
input() function in an eval() function! 
Basically saying: 'get the input and make it a value'. """

item_quantity = eval(input('How many do you want to buy? '))
# another number

subtotal = item_price * item_quantity
# we can do math with the numbers stored in these variables

tax_rate = 0.0825
# this is the sales tax rate in Texas (8.25%).

tax_amount = subtotal * tax_rate
# math operations like multiplication '*'

total = subtotal + tax_amount
# and addition (-)

print("To buy", item_quantity, item_name, "will cost", total,
    "dollars (after tax). \n")
"""We are all familiar with the print statement. 
The statement above is split across two lines, notice the indentation 
indicating that the previous line is continuing. """

print("And now for something completely different! Python doing math!")
""" A number with a decimal value is called a 'floating point number'
or a 'float' for short. The variable 'tax_rate' from above is an example
of a float. """
a_decimal = 0.0825
another_float = 2.0

""" A number without a decimal is call an 'integer' or an 'int' for
short. The variable 'a_whole_number' as definied below is an int. """
a_whole_number = 2
another_integer = 5
""" Python can tell the difference between an integer and a float, and
it will usually treat variables appropriately based on the value they
hold."""

"""We can do many mathematical operations on numbers in Python"""
print("Addition: 5 + 2 =", (another_integer + a_whole_number))
print("Subtraction: 5 - 2 =", (another_integer - a_whole_number))
print("Multiplication: 5 * 2 =", (another_integer * a_whole_number))
print("Division: 5 / 2 =", (another_integer / a_whole_number))

"""There are even some unfamilar operations"""
print("Find Remainder from division: 5 % 2 =",
    (another_integer % a_whole_number))
# This is another split line.
# Notice I split it after a comma within a set of (parenteses), 
# and I indented the continued line.

