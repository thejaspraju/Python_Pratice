"""
Write a Python program to count number of items in a dictionary value
that is a list.
"""

from typing import Dict

def countValues(my_dict : Dict)-> int:
    count = 0
    for values in my_dict.values():
        if type(values) == list:
            for x in values:
                count = count+ 1
        else:
            count = count + 1
    return count


Dict1 = { 'M1' : [67, 79, 90, 73, 36], 'M2' : [89, 67, 84], 'M3' : [82, 57],'M4' : 34 }
print(countValues(Dict1))