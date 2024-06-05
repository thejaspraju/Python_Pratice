"""
 Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original
list. Using slicing logic.
"""
from typing import List


def listLastNSlice(lst: List, n: int):
    l = len(lst)
    print(lst[l - n :])


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
listLastNSlice(my_list, 2)