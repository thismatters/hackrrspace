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
		return str(self.name) + ' (level ' + str(self.level) + (
			') has ' + str(self.eagle_bucks) + ' eagle bucks.')
	# notice that all the functions above belong to the ActonStudent 
	#   class. These functions will be available for all ActonStudent 
	#   objects when they are created.


# We should all be familiar with this
def ask_user_for_a_number(question="Which one (enter the number)? "):
    a_number = None
    while not a_number:
        try:
            a_number = eval(input(question))
        except NameError:
            print("Please enter a number!!")
    return a_number

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
		student = choose_student_from_list(students)
		print("What did {0} do?".format(student.name))
		print("1 >> Gained eagle buck(s)")
		print("2 >> Lost eagle buck(s)")
		print("3 >> Traded eagle buck(s) to ...")
		action = ask_user_for_a_number("What action? ")
		
	if selection is 4:
		for student in students:
			print(student)
	