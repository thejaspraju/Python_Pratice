"""
Write a function that takes a dictionary and a key, and returns True if
the key is found in the dictionary, otherwise False.
"""

from typing import Dict

def iskeypresent(my_dict : Dict, key) -> bool:
    for key in my_dict:
        return True;
    else:
        return False
    
my_dict = {"name": "Anirudh", "age": 56, "gender": "Male"}
print(iskeypresent(my_dict, "xyz"))
    