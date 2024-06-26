from typing import List

"""
Time Complexity = O(n)
Space Complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        n = len(nums)
        k %= n  # Handle cases where k > n

        print(reverse(0, n - 1))  # Reverse the entire array
        print(reverse(0, k - 1))  # Reverse the first k elements
        print(reverse(k, n - 1))  # Reverse the remaining elements
