"""
. Write a Python program to Convert two lists into a dictionary
"""

from typing import Dict ,List

def listtoDict(lst1:List,lst2:List) -> Dict:
    new_dict = zip(lst1,lst2)
    return new_dict

keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = listtoDict(keys, values)
print(set(my_dict))

##################### Method 2
from typing import Dict, List

def convertToDictionary(lst1: List, lst2: List) -> Dict:
    my_dict = {}
    for i in range(len(lst1)):
        my_dict[lst1[i]] = lst2[i]
    return my_dict

keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = convertToDictionary(keys, values)
print(my_dict)