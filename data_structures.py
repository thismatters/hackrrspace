""" In the last file (functional_programming.py) we learned about 
functions and how they can be utilized to reduce the amount of code we 
repeat in a program. In this file we will explore a few ways in which 
we can organize data. 

The simplest data structure in Python is the 'tuple'. A tuple is a 
collection of data surrounded in parenteses.
"""
this_is_a_tuple = (3, 5)

""" Here we are able to store these two values to a single variable, if 
necessary we can 'reference' the tuple using the 'index' of the data we 
want:
"""
print("The first value in the tuple is", this_is_a_tuple[0])
# the 'index' of the first value is always 0. 
#   This will take some getting used to
print("The second value in the tuple is", this_is_a_tuple[1])

""" We can also 'unpack' the tuple to assign each value its own 
variable:
"""
val_1, val_2 = this_is_a_tuple
print("Once again the first value in the tuple is", val_1)
print("Once again the second value in the tuple is", val_2)

# I'll just put this here
def ask_user_for_a_number(question):
    a_number = None
    while not a_number:
        try:
            a_number = eval(input(question))
        except NameError:
            print("Please enter a number!!")
    return a_number
a_number = ask_user_for_a_number("Pick a number: ")

""" We can do comparisons against the tuple to see what is in it:
"""
if a_number in this_is_a_tuple:
    print("The number you chose is 'in' the tuple!")
else:
    print("The number you chose is not 'in' the tuple!")

""" Within the context of an if-statement the 'in' keyword tells Python 
to look into this_is_a_tuple to see if a_number is contained in there. 
If a_number is contained in this_is_a_tuple then the statement will 
evaluate as true.

The 'in' keyword behaves a little differently in for-loops.
"""
print("\nFor the last time, the values in the tuple are:")
for value in this_is_a_tuple:
    print("value:", value)
""" In the context of a for loop, the 'in' keyword will cause the loop 
to iterate once for every element in the tuple. On each iteration the 
variable preceeding the 'in' will take (in order) a value stored in the 
tuple. 

Tuples can be 'nested', meaning that a tuple can hold a tuple.
"""
desserts = ((1, 'ice cream'), (2, 'cake'), (3, 'pie'), 
              (4, 'cookies'), (5, 'pudding'))
# I can split this line at a comma as long as I indent it well.

""" This 'nested' tuple can be used to print a selection menu easily! 
Here I'll use the 'in' keyword and the 'unpack' functionality to look 
at each part of that tuple independently.
"""
print("\nMake a selection from the choices below!")
for number, dessert in desserts:
    print(number, ': ', dessert, sep='')
selection = input('Choose: ')

""" Tuples are pretty great, but they are limited. For one, they are 
'immutable', which means that they cannot be changed. I cannot change 
the second value in this_is_a_tuple to be 6 nor can I add a value to 
the tuple 'desserts', instead I would have to make a new tuple. 

There is another data structure called a 'list', which does allow us 
to make modifications. A list can be defined using brackets '[]' or by 
calling the 'list()' function.
"""
an_empty_list = []
another_empty_list = list()
ingredients = ['potato', 'onion', 'carrot', 'broccoli', 
               'bell pepper', 'tofu']
# we can also define a list with stuff already in it as we did above.

print("\nNow let's think about a main course, here are some ingredients.")
suggestion = None
while not suggestion:
    for ingredient in ingredients:
        print(ingredient, end=", ", sep="")
    suggestion = input("\nSuggest an additional ingredient (enter q to stop): ")
    if suggestion == 'q':
        break
    if suggestion in ingredients:
        print("That is already an ingredient in the list")
        suggestion = None
    else:
        print("Adding", suggestion, "to the ingredients list")
        ingredients.append(suggestion)
        suggestion = None
""" The 'append()' function is specific to 'list' objects it will add 
the argument (in this case 'suggestion') to the end of the list.

There are many more functions that operate on list() objects. They can 
be found in the docs:
    https://docs.python.org/3.4/tutorial/datastructures.html
"""

print("Here is the final ingredient list:")
for ingredient in ingredients:
    print(ingredient, end=',\n')

""" There is another type of data structure called a 'dictionary' that 
we will discuss in the next file, for now see the task below!
"""

"""
***** TASK *****
In another file write a program that will allow the user to enter the 
names of all the people in the class, storing those names in a list as 
they are entered. Allow the user to exit the program as was done above 
(in the 'ingredients' block of code). When the user is done print the 
names to the screen.

call this file "list_classmates.py"

Go!
"""