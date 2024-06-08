"""
Write a Python program to create a dictionary of keys x, y, and z where
each key has as value a list from 11-20, 21-30, and 31-40 respectively.
Access the fifth value of each key from the dictionary.
"""
from typing import Dict


my_dict = {
    'x': list(range(11,21)),
    'y': list(range(21,31)),
    'z': list(range(31,41))
    }

fifth_value_X = my_dict['x'][5]
fifth_value_y = my_dict['y'][5]
fifth_value_z = my_dict['z'][5]

print(f"The fifth value of key 'x' is: {fifth_value_X}")
print(f"The fifth value of key 'y' is: {fifth_value_y}")
print(f"The fifth value of key 'z' is: {fifth_value_z}")