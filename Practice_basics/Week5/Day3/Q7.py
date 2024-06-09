"""
Create a Python program to find the difference between two
dictionaries.
First dictionary: {'a': 1,
'b': 2,
'c': 3}
Second dictionary: {'b': 2,
'c': 4,
'd': 5}
OUTPUT:
Keys present only in the first dictionary: ['a']
Keys present only in the second dictionary: ['d']
Keys present in both dictionaries: [’b’,‘c’]

"""
from typing import Dict

def compareDict(dct1:Dict,dct2:Dict):
    present_dict1 = []
    present_both = []
    for key in dct1.keys():
        if key not in dct2:
            present_dict1.append(key)
        else:
            present_both.append(key)
    present_dict2 = []
    for k in dct2:
        if k not in dct1:
            present_dict2.append(k)

    print(f"Keys present only in the first dictionary: {present_dict1}")
    print(f"Keys present only in the second dictionary: {present_dict2}")
    print(f"Keys present in both dictionaries: {present_both}")


compareDict({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5})