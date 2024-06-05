"""
Write a program to remove the nth index element from a list using a
function.
"""
from typing import List

def remove(lst:List,position)-> None:
    index = position
    print(f"the list before removing{lst}")
    lst.remove(lst[index])
    print(f"the lst after removing : {lst}")

my_list = [34,2,1,4,6,6,32,1,2,3,41,67,54,78]
remove(my_list,5)

#################### Code
def removeNth(lst: List, n: int) -> None:
    lst.pop(n)


my_list = [9008, 9102, 4311, 222, 98]
removeNth(my_list, 2)
print(my_list)
