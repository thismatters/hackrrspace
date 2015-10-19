""" We have learned about variables already. We know how to assign them,
how to read them, and how to compare them. Now we will think about a
concept called 'scope', which determines where variables are accesible.
"""

def scope_illustration():
    variable2 = 7
    variable3 = 2
    # variable3 is defined within this function; it will not be
    #    available outside this function
    print('inside the function variable1 is', variable1)
    # since variable1 was defined before this function was invoked it is
    #    available within this function
    print('inside the function variable2 is', variable2)
    print('inside the function variable3 is', variable3)

variable1 = 5
variable2 = 8
scope_illustration()  # this is where the function is 'invoked'
# invoking a function is the same as executing a function
print('outside the function variable1 is', variable1)
print('outside the function variable2 is', variable2)
print('outside the function variable3 is', variable3)
