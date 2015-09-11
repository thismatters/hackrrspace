""" The last file (data_structures.py) introduced a couple of built-in
types that permit us to group data together and store them as a single
variable. In this file we will focus on another data structure, namely
the 'dictionary' or 'dict' for short.

An empty dict can be created with either braces '{}' or with the dict()
function:
"""
an_empty_dict = {}
another_empty_dict = dict()

""" The useful feature of a dictionary is that it allows us to store
data based on key-value pairs, and we can use those keys to reference
the values. A dict lends itself well to describing something with as
much detail as we wish. For instance I can describe my cat thusly:
"""
lucy = {
    'type': 'cat',
    'subtype': 'calico',
    'gender': 'female',
    'size': 'very large',
    'age': 6,
}

""" As we see, the dictionary can hold information that has context. A
list with the same information can be created, but it will be hard to
make sense of that information without the association between the
'key' (e.g. name) and the 'value' (e.g. Lucy).

A dictionary is 'mutable' which means we can add to it or change it
when we need to. Here we'll add some information to the dictionary
describing my cat.
"""
lucy['pretty'] = True
lucy['age'] = 7
""" This adds a new key (pretty) to the dictionary with the associated
value (True). The next line updates the existing key (age) with a new
age.

Just like lists, dictionaries are 'iteratable' which means we can use
them in a for loop. To do this we can use the 'items()' function for
the dictionary.
"""
print("I have a cat named lucy, details below!")
for key, value in lucy.items():
    print(key, "is", value)

""" When you look at the output from the for loop above you might
notice that the fields are in a different order than when I typed them
in. This is to be expected, since the data in a dictionary are stored
by key-value pairs the order in which they are stored is irrelevant.

These next few lines are just setting up for the structre that appears
later. This is a list of tuples! See if you can follow what we do with
this later; one of your tasks later will be to explain it to me.
"""
field_questions = [('name', "What is your pet's name? "),
                   ('type', "What type of animal is {name}? "),
                   ('subtype', "What type of {type} is {name}? "),
                   ('gender', "Is {name} a female or male? "),
                   ('size', "How big is {name}? "),
                   ('age', "How old is {name}? "),
                   ('pretty', "Is {name} pretty? ")]

print("\nTell me about your pet!")
users_pet = dict()
for field, question in field_questions:
    users_pet[field] = input(question.format(**users_pet))

""" Just like tuples (and lists), dictionaries can be 'nested' meaning
that you can store a dictionary within a dictionary! This nesting
ability makes it really easy to store information about all the pets we
know using only one variable!
"""
pets = {
    'Antiope': {
        'type': 'ferret',
        'subtype': 'albino',
        'gender': 'female',
        'size': 'standard',
        'age': 4,
    },
    'Persephone': {
        'type': 'ferret',
        'subtype': 'standard',
        'gender': 'female',
        'size': 'standard',
        'age': 4,
    }
}

""" Oh yeah, let's not forget about Lucy and your pet!
"""
pets['Lucy'] = lucy
pets[users_pet['name']] = users_pet

print("\nThank you for telling me about your pet.")
print("These are all the pets I know:")
for name, pet in pets.items():
    print('\t', name, ':', sep='')
    for key, value in pet.items():
        print('\t\t', key, 'is', value)

"""
***** TASKS *****
In another file write a program that will gather information from the
user about something of your choosing! You must choose a subject which
you can ask at least four questions about. Gather the data into a
dictionary of dictionaries like 'pets' from above.

Go!
"""