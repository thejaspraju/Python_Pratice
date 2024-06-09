"""
Write a Python program to sort a dictionary by its keys in ascending
order.
"""

from typing import Dict

def sortByKeys(my_dict:Dict)->Dict:
    return dict(sorted(my_dict.items(),key = lambda x:x[0]))

my_dict = {"b": 2, "a": 1, "c": 3}

result = sortByKeys(my_dict)

print(my_dict)