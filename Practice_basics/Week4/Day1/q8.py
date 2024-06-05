"""
 Take 10 integer inputs from user and store them in a list. Now, copy all
the elements in another list but in reverse order.
"""
from typing import List

my_lst : List[int] = []

for i in range(10):
    num : int = int(input("Enter the number : "))
    my_lst.append(num)

reverse_lst = []
for i in range(len(my_lst) -1 , -1 ,-1):
    reverse_lst.append(my_lst[i])

print(reverse_lst)