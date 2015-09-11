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
	def __init__(self, name=None, age=None, level=None, eagle_bucks=0):
		""" The __init__ function is called when an object is created,
		we call the process of creating an object 'instantiation'.
		Later when we create an ActonStudent object we will pass three
		arguments (name, age, level, and eagle_bucks). The first
		argument listed: 'self', is a reference to the object that is
		being created. """
		self._name = name
		self._age = age
		self._level = level
		self._eagle_bucks = eagle_bucks
		""" Here, we are storing the information passed during
		instantiation to the object. """

	def is_evil_ducks(self):
		""" is_evil_ducks() will return a boolean, True if the student is
		in evil ducks. """
		evil_ducks = False
		if self._eagle_bucks < 0:
			evil_ducks = True
		return evil_ducks

	def earned_eagle_bucks(self, count=1):
		""" earned_eagle_bucks() will increase the student's eagle buck
		count, by count. Returns the student's updated eagle buck
		count."""
		self._eagle_bucks += count
		return self._eagle_bucks

	def lost_eagle_bucks(self, count=1):
		""" lost_eagle_bucks() will decrease teh student's eagle buck
		count, by count. Returns the student's updated eagle buck
		count."""
		self._eagle_bucks -= count
		return self._eagle_bucks

	def __str__(self):
		""" This (along with __init__) are 'special methods'. This
		function will be called when an ActonStudent needs to be
		represented by a string."""
		return str(self._name) + ' (level' + str(self._level) + (
			') has ' + str(self._eagle_bucks) + ' eagle bucks.')

if __name__ == '__main__':
	keep_going = True
	while keep_going:
		# print the menu
			# Add student
			#
		# process the selection
