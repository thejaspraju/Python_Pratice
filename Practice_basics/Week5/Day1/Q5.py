"""
Write a Python program to check if a dictionary is empty or not.
"""
from typing import Dict

def isempty(dictionary : Dict) -> bool:

    #Method 1
    '''
    if not dictionary :
        return True:
    return False
    '''
    """
    #method 2
    if len(dictionary.keys()) == 0:
        return True
    return False
    """
    #Method 3
    count = 0
    for i in dictionary.keys():
        count += 1
    if count == 0:
        return True
    return False

print(isempty({}))
print(isempty({"name": "xyz"}))
