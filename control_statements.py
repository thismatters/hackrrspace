""" Last time (in variables_and_operators.py) we learned about some of 
the ways in which python can manipulate data, this time we will learn 
how python can do different things based on the data it has.
"""

secret_number = 7

guess = eval(input("Give me a number: "))

""" The 'if' statement is a way that we can control the flow of our 
program. It allows us to make comparisons and to cause the program to 
behave differently based on the outcome of those comparisons. """
if guess == secret_number:
    print("Good guess!")
    
""" Notice the syntax of the two lines above. The first line starts 
with the keyword 'if' which is followed by the 'condition' which is 
followed by a colon ':'. The second line is the 'block of code' to be 
executed if the condition is true; this block is indented to indicate 
that it belongs to the if statement. Every indented line that follows 
the if statement will be executed if the condition is true.

Did you see that the condition in the if statement used two equal 
signs? 
    guess == secret_number

The double equal '==' is different from the single equal '='. 

The single equal is an _assignment operator_ while the double equal is 
a _comparison operator_. Comparison operators evaluate the truth of a 
statement and return either 'True' or 'False'.

Here we will use another comparison operator, namely 'greater than' 
"""
if guess > secret_number:
    print("Too high!")

""" and here we use 'less than' """
if guess < secret_number:
    print("Too low!")

""" There are a few other comparison operators we could think about:
'>=': Greater than or equal to
'<=': Less than or equal to
'!=': Not equal
More information about comparison operators is available in the docs:
    https://docs.python.org/3.4/library/stdtypes.html#comparisons
"""
if guess != secret_number: # if guess does not equal secret_number do: 
    print("Not a good guess")

second_guess = eval(input("Guess again: "))

""" The if statement has some other functionality to explore. The 
behavior we have seen so far is that we can execute a block of code if 
a condition evaluates to True, but we can also evaluate code if the 
condition is False by using the 'else' keyword.
"""
if second_guess == secret_number:
    # this executes if second_guess is equal to secret_number
    print("Good guess!")
else:
    # this executes if second_guess is not equal to secret_number
    print("Bad guess!")
    if second_guess > secret_number:
        # Another level of indentation!!
        # this will execute if second_guess is greater than secret_number
        print("Too high")
    else:
        # this will execute if second_guess is not greater than 
        #  secret_number (also second_guess must not be equal to secret 
        #  number due to the earlier if statement)
        print("Too low")

""" There is another keyword associated with 'if', specifially 'elif'. 
This is short for 'else if'. We could use that to simplify the above 
example.
"""

third_guess = eval(input("Guess again: "))
if third_guess == secret_number:
    # this executes if second_guess is equal to secret_number
    print("Good guess!")
elif third_guess > secret_number:
    # this will execute if the first condtion was false and the second
    #  condition was true
    print("Too high")
else:
    # this will execute if both of the previous conditions are False
    print("Too low")

""" 
***** TASK *****
In another file write a program to tell me which player won the game. 

call this file 'pvp.py'

Go! (Start with the two lines below)
"""
# player_1_score = eval(input("Player 1 score: "))
# player_2_score = eval(input("Player 2 score: "))


"""
***** TASK *****
In another file write a program to tell me whether the number is 
even or odd.

call this file 'even_or_odd.py'

Go! (Start with the line below)
"""
# the_number = eval(input("Tell me a number: "))