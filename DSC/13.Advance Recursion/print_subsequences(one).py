"""
Print all the subsequences where sum=K.
Generate only 1

Time complexity -> O(2^n)
"""

from typing import List


def backtrack(subset: List[int], index: int, total: int):
    if total == k:
        result.append(subset.copy())
        return True
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    if backtrack(subset, index + 1, Sum):
        return True
    e = subset.pop()
    Sum -= e
    return backtrack(subset, index + 1, Sum)


result = []
nums = [3,1,2]
k = 3
backtrack([], 0, 0)
print(result)