"""
Make your own list of numbers. Ask a start and end position from User.
Print the list from start position to end position using without using Slicing.
"""
from typing import List

def listslice(lst:List,start:int,end:int):
    result = []
    for i in range(start,end+1):
        result.append(lst[i])
    return result

my_lst = ["Thejas", 6,4,110.654,True,-54]
print(listslice(my_lst,2,4))