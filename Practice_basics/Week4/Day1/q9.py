"""
Make a list. Write a simple program for addition of the 2nd element
from start and 2nd element from the end.
"""
from typing import List

def sumofelemnts(lst:List)->None:
    result = lst[1] + lst [-2]
    print(f"the sum of 2nd and the last 2nd = {result}")

my_list = [1,2,3,4,5,6,7]
sumofelemnts(my_list)