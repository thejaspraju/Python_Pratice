"""

Q4. Write a Python Program to find sum and average of List in Python.
"""
from typing import List

def sumAvg(lst : List):
    avg1 = 0
    sum1 = sum(lst)
    avg1 = sum1/ len(lst)
    print(f"the sum = {sum1}")
    print(f"Average is = {avg1}")

my_list = [1,2,3,4]
sumAvg(my_list)
##################### Code and Debug
def sumAverage(lst: List[int]) -> None:
    total = 0
    for i in lst:
        total = total + i
    print(f"Total = {total}")

    average = total / len(lst)
    print(f"Average = {average}")


my_list = [34, 96, 34, 65.34, 51, 27, 96.12, 96, 11, 34]
sumAverage(my_list)

