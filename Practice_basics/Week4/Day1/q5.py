"""
Q5. Write a program to put all the common elements (in 2 lists) in another
list and print it using function.
"""

from typing import List

def compare(lst1 : List ,lst2 : List) -> list:
    result = []
    for i in lst1:
        if i in lst2:
            result.append(i)
    return result

lsit1 = [1,2,3,4]
list2 = [1,3,6,7]
print(compare(lsit1,list2)) 

################ Method 2
def common(lst1: List, lst2: List) -> List:
    result = []
    for i in lst1:
        # Check if i is in lst2 also
        if i in lst2:
            result.append(i)
    return result


my_list1 = ["Anirudh", "xyz", 98, 11.908, 93, -100]
my_list2 = [9008, 9102, 4311, 222, 98]

x = common(my_list1, my_list2)
print(x)
