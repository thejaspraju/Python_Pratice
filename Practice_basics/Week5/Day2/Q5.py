"""
Given a dictionary, write a function that returns a new dictionary
containing only the keys that have values of type str.
"""
from typing import Dict

def new_dictionary(my_dict : Dict)->Dict:
    new_dictionary = {}
    for key,value in my_dict.items():
        if type(value) == str:
            new_dictionary[key] = value
    return new_dictionary

my_dict = {"name": "Thejas", "age": 56, "gender": "Male","height" : 6.2}
print(new_dictionary(my_dict))

####### Method 2
def filter_string_value(d):
    return {k:v for k, v in d.items() if isinstance(v,str)}

my_dict = {"name": "Thejas", "age": 56, "gender": "Male","height" : 6.2}
print(filter_string_value(my_dict))