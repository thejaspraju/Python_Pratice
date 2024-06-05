"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""

# This method will work only if there are no duplicates in the array
from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    # Sort the array
    a.sort()

    # Second minimum will be on 1st index
    # Second largest will be on last second index
    return [a[-2], a[1]]

my_lst = [34,21,5,32,65,80,97,53,2]
print(getSecondOrderElements(len(my_lst),my_lst))