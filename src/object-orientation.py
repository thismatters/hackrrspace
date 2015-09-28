""" In the last file (dictionaries.py) we learned about dictionaries,
which are really good at storing information based on key-value pairs.
This gives the data context so we can better understand it. In this
file we will explore 'objects', which allow us the ultimate ability to
define data with specific context that we can extend and access.

Objects can be whatever we need. In this file we will create an object
to represent students of Acton Academy.

To define an object we will use the 'class' keyword:
"""


class ActonStudent:
	""" It is typical to use CamelCase (each word capitalized with no
		spaces) for object names."""
	def __init__(self, name=None, age=None, level=1, eagle_bucks=0):
		""" The __init__ function (short for 'initialize') is called 
		when an object is created, we call the process of creating an 
		object 'instantiation'. Later when we create an ActonStudent 
		object we will pass four (or fewer) arguments (name, age, level,
		and eagle_bucks). The first argument listed: 'self', is a 
		reference to the object that is being created. """
		self.name = name
		self.age = age
		self.level = level
		self.eagle_bucks = eagle_bucks
		# Here, we are storing the information passed to the object 
		#   during instantiation.  

	def is_evil_ducks(self):
		""" is_evil_ducks() will return a boolean, True if the student is
		in evil ducks. """
		evil_ducks = False
		if self.eagle_bucks < 0:
			evil_ducks = True
		return evil_ducks

	def earned_eagle_bucks(self, count=1):
		""" earned_eagle_bucks() will increase the student's eagle buck
		count, by count. Returns the student's updated eagle buck
		count."""
		self.eagle_bucks += count
		return self.eagle_bucks

	def lost_eagle_bucks(self, count=1):
		""" lost_eagle_bucks() will decrease the student's eagle buck
		count, by count. Returns the student's updated eagle buck
		count."""
		self.eagle_bucks -= count
		return self.eagle_bucks

	def lvl_up(self):
		""" lvl_up() will increase the student's level by one; returns 
		student's new level. """
		self.level += 1
		return self.level

	def __str__(self):
		""" This (along with __init__) are 'special methods'. This
		function will be called when an ActonStudent needs to be
		represented by a string."""
		string_value = ''
		suffix = ''
		if self.is_evil_ducks():
			string_value += '<EVILDUCKS> '
			suffix += ' </EVILDUCKS>'
		string_value += str(self.name) + ' (level ' + str(self.level) + (
			') has ' + str(self.eagle_bucks) + ' eagle bucks.')
		string_value += suffix
		return string_value
	# notice that all the functions above belong to the ActonStudent 
	#   class. These functions will be available for all ActonStudent 
	#   objects when they are created.


# We should all be familiar with this
def ask_user_for_a_number(question="Which one (enter the number)? "):
    a_number = None
    while a_number is None:
        try:
            a_number = eval(input(question))
        except NameError:
            print("Please enter a number!!")
            a_number = None
    return a_number

# This is a new one, can you see what is happening here? 
def choose_student_from_list(student_list):
	selection = None
	for student_number, student in enumerate(student_list):
		print(student_number, '>>', student.name)
	selection = ask_user_for_a_number("Which student (enter the nubmer)? ")
	return student_list[selection]

students = list()
keep_going = True
while keep_going:
	print("\nWhat would you like to do? (options below)")
	print('1 > Add new students')
	print('2 > Mange Eagle Bucks')
	print('3 > Level up')
	print('4 > Display Students')
	print('5 > Quit')
	selection = ask_user_for_a_number()
	print('\n')
	if selection > 5 or selection < 1:
		print("INVALID SELECTION")
		# the built-in 'continue' keyword below will skip past the rest 
		#   of the code in this block and start the next iteration of  
		#   the loop
		continue
	if selection is 5:
		print("Goodbye")
		keep_going = False
		break
	if selection is 1:
		print("Adding new student! ")
		new_student_name = input("What is the new student's name? ")
		new_student_age = ask_user_for_a_number("What is the student's age? ")
		new_student_level = ask_user_for_a_number("What level? ")

		# This is the part where we instantiate a new student.
		new_student = ActonStudent(name=new_student_name, 
								   age=new_student_age,
								   level=new_student_level)
		# When we call ActonStudent, Python will create a new object 
		#   and send a reference to that new object and all the other 
		#   information (name, age, etc.) to the __init__ function we 
		#   looked at earlier.
		students.append(new_student)
		print("A new student has been added! Their details follow")
		print(new_student)
	if selection is 2:
		print("Which student?")
		student = choose_student_from_list(students)
		print("What did {0} do?".format(student.name))
		print("1 >> Gained eagle buck(s)")
		print("2 >> Lost eagle buck(s)")
		print("3 >> Traded eagle buck(s) to ...")
		action = ask_user_for_a_number("What action? ")
		if action is 3:
			print("Which student did {0} give Eagle Bucks to? ".format(
				student.name))
			recipient = choose_student_from_list(students)
		if action in (1, 2, 3):
			number = ask_user_for_a_number("How many? ")
		if action is 1:
			student.earned_eagle_bucks(number)
		if action in (2, 3):
			student.lost_eagle_bucks(number)
		if action is 3:
			recipient.earned_eagle_bucks(number)
	if selection is 3:
		print("Which student?")
		student = choose_student_from_list(students)
		print("{0} is now level {1}".format(student.name, student.lvl_up()))
	if selection is 4:
		for student in students:
			print(student)
"""
Writing a menu-based program typically requires this sort of 
if-statement structure. They can be cumbersome to write, thankfully 
most modern programs aren't menu-based. Soon we will move into event 
driven programming!!

You might notice that every time you quit this program all the student 
data we enter on the command line goes away. Python automatically 
deletes unused objects to free up computer memory. This would be 
troublesome if we were actually trying to track student progress here 
at Acton. Thankfully there is a way that we can store information that 
will be more persistent. So called 'databases' will hold information 
independently from the programs we write, in the next file we will 
explore databases!
"""

"""
***** TASK *****
The function choose_student_from_list() has a bug. Your task is to 
figure out what conditions will cause that function to crash, and to 
figure out a way to fix the bug.

Go!
"""	

"""
***** TASK *****
Expand the ActonStudent class (here in this file), such that it can be 
used to track what books the student has read. Consider which data 
structure is appropriate to store this information and write functions 
to get this information into the student object.

Go!
"""
