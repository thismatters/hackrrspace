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
cat = {
    'name': 'lucy',
    'gender': 'female',
    'type': 'calico',
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
cat['pretty'] = True
cat['age'] = 7
""" This adds a new key (pretty) to the dictionary with the associated 
value (True). The next line updates the existing key (age) with a new 
age.

Just like lists, dictionaries are 'iteratable' which means we can use 
them in a for loop. To do this we can use the 'items()' function for 
the dictionary.
"""
for key, value in cat.items():
    print(key, "is", value) 

""" When you look at the output from the for loop above you might 
notice that the fields are in a different order than when I typed them 
in. This is to be expected, since the data in a dictionary are stored 
by key-value pairs the order in which they are stored is irrelevant.  
"""