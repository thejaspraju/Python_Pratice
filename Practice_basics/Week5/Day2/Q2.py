"""
 Given two dictionaries, write a function to merge them into a new
dictionary. If there is any overlap of keys, the value from the second
dictionary should overwrite the one from the first dictionary.

"""
from typing import Dict

def mergeDict (dict1:Dict,dict2:Dict) -> Dict:
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = (value)
    return merged

print(
    mergeDict(
        {"apple": 3, "banana": 5, "cherry": 7},
        {"banana": 8, "orange": 10, "apple": 9},
    )
)