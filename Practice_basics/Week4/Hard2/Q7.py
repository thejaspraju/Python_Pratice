"""
Write a Python code to find the second largest element in a list without
sorting.
"""
from typing import List

def secondLargest(lst : List[int]):
    if len(lst) < 2 :
        return "Not enough elements"
    
    largest = secondLargest = float("-inf")

    for num in lst:
        if num > largest :
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
    
    if secondLargest == float("-inf"):
        return "There is no second largest"
    else:
        return secondLargest

nums = [12, 74, -89, 96, -98, -96, 52]
result = secondLargest(nums)
print(f"Second largest element = {result}")