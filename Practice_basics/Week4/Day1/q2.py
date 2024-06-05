"""
Write a function to remove duplicates from a list and print them.
"""
from typing import List
def removeduplicates(lst : List[int])->None:
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)

my_list = [1,2,4,3,2,3,4,5,4,6,7,1,2,4,3]
removeduplicates(my_list)