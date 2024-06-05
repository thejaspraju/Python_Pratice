"""
 Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original list
but in reverse order. Using slicing logic
"""
from typing import List


# Method 1
# def reverselistLastNSlice(lst: List, n: int):
#     l = len(lst)
#     result = lst[l - n :]
#     result.reverse()
#     print(result)


# Method 2
def reverselistLastNSlice(lst: List, n: int):
    l = len(lst)
    result = lst[: l - n - 1 : -1]
    print(result)


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
reverselistLastNSlice(my_list, 3)
