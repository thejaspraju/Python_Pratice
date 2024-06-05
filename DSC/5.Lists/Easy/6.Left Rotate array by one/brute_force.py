from sys import *
from collections import *
from math import *

"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)
"""


def rotateArray(arr: []) -> []:
    last_element = arr.pop(0)
    arr.append(last_element)
    return arr

my_lst = [4,5,6,1,2,3]
print(rotateArray(my_lst))