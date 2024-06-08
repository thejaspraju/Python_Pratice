"""
A Python dictionary contains List as a value. 
Write a Python program to clear the list values in the same dictionary.
Original Dictionary:{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:{'C1': [], 'C2': [], 'C3': []}
"""

from typing import Dict

def clearvalue(my_dict : Dict):
    for key in my_dict:
        my_dict[key] = []


original_dict = {"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]}

clearvalue(original_dict)

print(original_dict)
