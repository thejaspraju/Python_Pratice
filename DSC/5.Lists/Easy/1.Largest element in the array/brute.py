"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr) -> int:
    # Sort the elements first
    arr.sort()

    # Return the largest from the end
    return arr[-1]
my_list = [3,2,6,5,1,7,8,0]
print(largestElement(my_list))