""" Last time (in control_statements.py) we learned about the 
if-statement, and how it can control which blocks of code get executed.
This time we will learn how to make certain blocks of code execute many 
times. 

Before getting in to that let's learn about a new data type. 
In addition to numbers (integers and floats) and strings, there is also 
a type called 'Boolean'. A boolean variable is either True or False.
"""

boolean_variable = True
another_boolean_variable = False

""" Boolean variables are really useful for control statements:
"""

if boolean_variable:
    print("This line will ALWAYS be printed")
else:
    print("This line will NEVER be printed")

if another_boolean_variable:
    print("This line will also NEVER be printed")
else:
    print("This line will also ALWAYS be printed")

""" Now, on to looping structures. In the last lesson we gave the user 
three chances to guess the secret_number. This time we want to give 
them 5 guesses!! We could do this by copy-pasting the question asking 
block of code 5 times, but that's boring. Instead lets tell python to 
execute the code 5 times!
"""
secret_number = 42
for guesses_attempted in [1, 2, 3, 4, 5]:
    # this block of code will execute once for every number in the list above
    # with each pass the variable 'guesses_attempted' will take the next value in the list
    print("guess count:", guesses_attempted)
    guess = eval(input("What is your guess? "))
    if guess == secret_number:
        print("Good guess! It only took you", guesses_attempted, "guesses!")
        break;
        # break will stop the loop from executing when the number is guessed!!
    elif guess > secret_number:
        print("Too high, guess again.")
    else:
        print("Too low, guess again.")

""" There is a useful built-in function that we will use often with 
for-loops. It is called 'range()', and it will return a list of numbers 
within a range that the programmer specifies.
 
For instance:
range(5) returns [0, 1, 2, 3, 4]
range(10) returns [0, 1, 2, 3, 4, 6, 7, 8, 9]
range(1, 6) returns [1, 2, 3, 4, 5]
range(10, 5, -1) returns [10, 9, 8, 7, 6]

If you want more information on how range() works try searching 
'pyton range' on duckduckgo.

Let's use range() to give the user 5 more guesses. This time let's also 
track whether the user has guessed correctly so we will know later.
"""

guessed_correctly = False
for guesses_attempted in range(6, 11):
    # this block of code will execute once for every number in the list above
    # with each pass the variable 'guesses_attempted' will take the next value in the list
    print("guess count:", guesses_attempted)
    guess = eval(input("What is your guess? "))
    if guess == secret_number:
        print("Good guess! It took you", guesses_attempted, "guesses!")
        guessed_correctly = True
        # they guessed correctly, lets set that variable to 'True'!
        break;
    elif guess > secret_number:
        print("Too high, guess again.")
    else:
        print("Too low, guess again.")

""" It might take the user forever to guess the right number if they 
haven't already. This is the perfect time to introduce another looping 
structure. The 'while' loop will execute a block of code until it is 
told not to continue.
"""

while guessed_correctly is not True:
    # 'is' can be used in place of '==' in most cases and
    # 'is not' can be used in place of '!=' in most cases.
    guesses_attempted += 1
    # this is the same as 'guesses_attempted = guesses_attempted + 1'
    print("guess count:", guesses_attempted)
    guess = eval(input("What is your guess? "))
    if guess == secret_number:
        print("Finally! It took you", guesses_attempted, "guesses!?")
        guessed_correctly = True
    elif guess > secret_number:
        print("Too high, guess again.")
    else:
        print("Too low, guess again.")

""" If you get tired of guessing you can stop your program by 
pressing CTRL+C. This will be useful as you experiment with looping 
structures, from time to time you might accidentally need to escape 
from an _infinite loop_ like the one commented out below.
"""
# while True:
#     print("this is the program that never ends,")
#     print("it just goes on and on my friends.")


"""
***** TASK *****
In another file write a program using a for loop and the range statement
to print the first 15 odd numbers (starting with 1) to the screen.

call this file 'odd_ducks.py'

Go!
"""

"""
***** TASK *****
Modify the file you made earlier called 'even_or_odd.py' so that it 
will ask for a number and return an answer repeatedly until the user 
inputs a negative number.

Go!
"""