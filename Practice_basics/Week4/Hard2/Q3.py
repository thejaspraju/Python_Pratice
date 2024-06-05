"""
Write a python program to check if the list contains three consecutive common numbers in Python.
"""

from typing import List

def isConsecutive(my_lsit : List[int]):
    for i in range (0 , len(my_lsit) -2):
        if my_lsit[i] == my_lsit[i+1] == my_lsit[i+2]:
            print(my_lsit[i])

isConsecutive([1, 2, 3, 4, 55, 55, 55, 6, 7, 7, 7])
isConsecutive([1, 2, 3, 4, 55, 55, 6, 7, 7])