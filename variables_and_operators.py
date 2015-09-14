""" Last time (in hello.py) we learned about variables and how they can
be set from inside the program and outside the program; all of
the variables in the last lesson were assigned strings. In this lesson
we will think about what other types of variables we can use. """

item_name = input('What do you want to buy? ')
# remember: input() will accept a string input

item_price = eval(input('How much does it cost? $'))
""" When we are expecting a number we tell Python by wrapping the
input() function in an eval() function!
Basically saying: 'get the string input and make it a value (number)'.

What happens if we don't type a number in there?
"""

item_quantity = eval(input('How many do you want to buy? '))
# another number

tax_rate = 0.0825
# This is the sales tax rate in Texas (8.25%).

subtotal = item_price * item_quantity
# we can do math with the numbers stored in these variables

tax_amount = subtotal * tax_rate
# math operations like multiplication '*'

total = subtotal + tax_amount
# and addition (-)

print("To buy", item_quantity, item_name, "will cost", total,
    "dollars (after tax).")
"""We are all familiar with the print statement.
The statement above is split across two lines, notice the indentation
indicating that the previous line is continuing.

An 'indentation' is 4 spaces '    '.
"""

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
hold. Many other programming languages aren't so savvy. """

"""We can do many mathematical operations on numbers in Python"""
print("\nAddition: 5 + 2 =", (another_integer + a_whole_number))
# what did that '\n' do??
print("Subtraction: 5 - 2 =", (another_integer - a_whole_number))
print("Multiplication: 5 * 2 =", (another_integer * a_whole_number))
print("Division: 5 / 2 =", (another_integer / a_whole_number))
print("Raise by Power: 5 ** 2 =", (another_integer ** a_whole_number))
# this is 5 to the power of 2 (or 5^2 might be more familiar)

"""There are even some unfamilar operations, the '%' is called 'modulo' """
print("Find Remainder from division: 5 % 2 =",
    (another_integer % a_whole_number))
# This is another split line.
# Notice I split it after a comma within a set of (parenteses),
# and I indented the continued line.

print("\nWait, show me that modulo again!!")
# there it is again! '\n'
print("8 % 3 =", (8 % 3))
print("92642 % 71 =", (92642 % 71))
print("8 % 2 =", (8 % 2))
""" The modulo operator may seem strange--and it is--but it is also
quite useful. For instance, knowing that 'another_integer % 2 = 1' tells
me that 'another_integer' is an odd number, because when I divide an
odd number by 2 there will always be a remainder of 1! Also notice that
'8 % 2 = 0', this means that 8 must be an even number.

More information on numerical operators is available in the docs:
    https://docs.python.org/3.4/library/stdtypes.html#numeric-types-int-float-complex
"""

print("\nIs there math with strings?")
# Yes, sorta!!
word = input("Give me a word: ")
another_word = input("Give me another word: ")
number = eval(input("Give me a number: "))

print("Concatenation: word + another_word =", (word + another_word))
print("Repetition: word * number =", (word * number))

"""
***** TASK *****
In another file write a program that will cause the following statement
to be printed to the screen 50 times (on 50 separate lines):

'I will always be a good hacker!'

call this file 'good_hacker.py'

Go!
"""

"""
***** TASK *****
In another file write a program that will cause the following statement
to be printed to the screen:

'I will be a really really really really really really good hacker!'

call this file 'really_good_hacker.py'.

To successfully complete this task the source code for your program
may only contain the word 'really' once! Extra whitespace in the output
is permitted if needed.

If you read the docs on the print statement you might be able to avoid
the extra whitespace.
    https://docs.python.org/3.4/library/functions.html#print
"""