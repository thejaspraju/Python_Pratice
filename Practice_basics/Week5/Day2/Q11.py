"""
Given a dictionary with key-value pairs, remove all the keys with
values greater than K, including mixed values.
"""
from typing import Dict

def remove_greater_k(my_dict:Dict,k:int):
    dict1 = my_dict.copy()
    key_remove = []
    for key,value in dict1.items():
        if type(value) == int and value > k:
            key_remove.append(key)
    for key in key_remove:
        dict1.pop(key)
    
    return dict1

test_dict1 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "xyzx": "CS"}
k = 1

output1 = remove_greater_k(test_dict1, k)
print(output1)

