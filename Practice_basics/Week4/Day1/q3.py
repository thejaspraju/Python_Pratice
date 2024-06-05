"""
 Write a Python function that takes two lists and returns True if they
have at least one common element.
"""

from typing import List

def comparelist(lst1 : List[int], lst2 : List[int]) -> bool:
    for num in lst1:
        if num in lst2:
            return True
        else:
            return False
        
lsit1 = [1,2,3,4,5]
list2 = [6,7,8,9,1]
print(comparelist(lsit1,list2))