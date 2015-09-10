""" In this program we will explore the idea of 'methods' or 'functions'
which allow us to write small bits of code that we can re-use easitly 
and quickly. In the last lesson we refined our ability to handle 
unexpected input, and as one of your tasks you wrote a program that will
continue asking the user to enter a number until they actually do so. 

It may have looked something like this:
"""
dining_partners = None
# _initializing_ this variable to None allows for simple syntax on the 
# while loop. A variable that is None will evaluate as false, while a 
# variable with a non-None value will evaulate as True
while not dining_partners:
    try:
        dining_partners = eval(input("How many people did you eat with? "))
    except NameError:
        print("I said a number!!")

""" Now this is a pretty easy bit of code; it's only 6 lines long and it
will ensure that the variable dining_partners definitely has a number 
before proceeding. However, every time we need another number from the 
user we will have to repeat these 6 lines almost exactly. 

It would be much more efficient if we could write this code once and 
tell python how to get to it. This is the basic idea of a 'function'. 
It is a bit of code that Pyhton knows how to execute. 

For instance we could write:
"""
def ask_user_for_a_number():
    a_number = None
    while not a_number:
        try:
            a_number = eval(input("Meal cost? "))
        except NameError:
            print("That's not a number!!")
    return a_number
""" The 'def' keyword is telling python to remember what follows as a 
definition. Python will remember the name 'ask_user_for_a_number' and 
whenever we 'call' that name Python will execute the indented code. 

When Python gets to the 'return' statement it will the contents of the 
variable 'a_number' back to wherever the function was called from.
"""
total_cost = 0
for diner in range(dining_partners):
    print("Diner ", diner, ":", sep='')
    cost = ask_user_for_a_number()
    total_cost += cost

print("The total meal cost is", total_cost, "before tax.")

""" Notice that every time we call 'ask_user_for_a_number' it will 
display the same question: 'Meal cost?'. To get around this we can pass 
an 'argument' to the function. This argument must be named in the 
function definition afterward it can be used in the indented part 
wherever we need it like so:
"""
def ask_user_for_a_number(question):
    a_number = None
    while not a_number:
        try:
            a_number = eval(input(question))
        except NameError:
            print("Please enter a number!!")
    return a_number

""" Now we can specify the question we want to ask when we call the 
'ask_user_for_a_number' function.
"""
tax_rate = ask_user_for_a_number("What is the tax rate? ")
tax_amount = total_cost * (tax_rate / 100)
total_cost += tax_amount

""" We can go one step further and specify a default question when 
declaring the function like so:
"""
def ask_user_for_a_number(question="How much did you leave for tip? "):
    a_number = None
    while not a_number:
        try:
            a_number = eval(input(question))
        except NameError:
            print("Please enter a number!!")
    return a_number

""" Now if we call 'ask_user_for_a_number' without specifying a 
question it will automatically ask the default question.
"""
tip_amount = ask_user_for_a_number()
total_cost += tip_amount
service_rating = ask_user_for_a_number("How was your service (1-5)? ")

print("The total spent on the meal was", total_cost)
if service_rating > 3:
    print("We're happy you enjoyed our service!")
else:
    print("We're sorry our service was not up to your expectations.")   

"""
***** TASK *****
Modify your 'advanced_tic_tac_toe.py' program to utilize functions. 
Create a function called 'draw_tic_tac_toe()' that will accept a single 
argument (size); this function must print the appropriately sized 
tic-tac-toe board. If no size is passed the function should default to 
size = 3

Go!
"""
