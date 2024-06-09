"""
Create a Python function to reverse a dictionary (swap keys and
values). Make sure the values are different.
Original dictionary: {'a': 1, 'b': 2, 'c': 3}
Reversed dictionary:
{1: 'a', 2: 'b', 3: 'c'}
"""
from typing import Dict

def reversekeyvalue(my_dict:Dict)->Dict:
    reversed_dict = {}
    for key,value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict

my_dict =  {'a': 1, 'b': 2, 'c': 3}
print(reversekeyvalue(my_dict))