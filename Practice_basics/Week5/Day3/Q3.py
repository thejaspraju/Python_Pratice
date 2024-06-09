"""
Write a Python program to print a dictionary line by line.
"""
from typing import Dict

def printDictline(my_dict : Dict):
    for key , value in my_dict.items():
        print(key)
        for k ,v in value.items():
            print(f"{k} : {v}")

printDictline(
    {
        "Sam": {"M1": 89, "M2": 56, "M3": 89},
        "Suresh": {"M1": 49, "M2": 96, "M3": 89},
    }
)
