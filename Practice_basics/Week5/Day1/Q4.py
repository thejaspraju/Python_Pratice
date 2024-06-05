"""
Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
"""
from typing import Dict

def createDict (n:int)-> Dict[int,int]:
    my_dict = {}
    for i in range (1,n+1):
        my_dict[i] = i**2
    return my_dict

print(createDict(5))