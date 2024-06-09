"""
Write a Python script to sort (ascending and descending) a dictionary
by value.
"""
from typing import Dict

def sortDictionary(my_dict:Dict, reverse = False):
    return dict(sorted(my_dict.items(),key = lambda x:x[1], reverse=reverse))

my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f"Ascending order = {sortDictionary(my_dict)}")
print(f"Descending order = {sortDictionary(my_dict,reverse=True)}")

