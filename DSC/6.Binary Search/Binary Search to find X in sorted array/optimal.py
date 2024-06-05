"""
Time complexity -> O(logn)
n is number of elements in nums

Space complexity -> O(1)
"""

from typing import List

def searchelement(nums:List[int],target:int)->int:
    n = len(nums)
    low = 0
    high = n-1
    while (low <= high):
        mid = (low+high) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1

my_list = [1,5,6,7,9,11,14,15,19,20]
print(searchelement(my_list,15))
    