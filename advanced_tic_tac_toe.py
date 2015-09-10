""" THIS IS A LEVEL TEST!

Last time we learned about looping structures, which are the last of the
essential programming techniques. There is much more to learn, but now 
you must show your mastery of sequential programming!

To become a lvl1 programmer you must create a program that will prompt 
the user for a number which will serve as the size, then create a 
tic-tac-toe board with that number of rows and columns.

Create your program in this file.

For instance if the user inputs that the size should be 4 the following 
board should be printed:

   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |   |

If the user indicates the size is 2 the board should look like this:

   |
---+---
   |

Hints: 
* Consider how many lines of text must be drawn for a board of 
size 4, how many must be drawn for a board of size 10?

* Consider the fact that alternating lines of text look same. All the 
odd rows are identical, and all the even rows are identical.

* Remember how to repeat a string? (see variables_and_operators.py)

* What is the smallest size of tic-tac-toe board that makes sense?
"""

size = eval(input("How big? "))