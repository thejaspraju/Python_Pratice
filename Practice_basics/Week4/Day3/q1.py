"""
 Create a function countOddEven that accepts an List of Integers and
print how many even and odd numbers are there.
"""
from typing import List
def countoddeven(nums : List)->None:
    odd = 0
    even = 0
    n = len(nums)
    for i in range (0 , n ):
        if nums[i] % 2 ==0:
            even+=1
        else:
            odd += 1
    print(f"Total Even number = {even}")
    print(f"Total odd number = {odd}")

my_list = [34,11,91,59,22,33]
countoddeven(my_list)

############################ Code debug
my_list = [43, 65, "Elon", "Ambani", False, 55.43]


i = len(my_list) - 1
while i > -1:
    print(my_list[i])
    i -= 1
