from typing import List

"""
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Space complexity = O(1)
"""

class solution:
    def check(self,nums:List[int])->bool:
        n = len(nums)
        print(n)
        # We will count the rotations, we know the array can rotated only 1 time
        # and can be sorted, if the rotation will be greater than 1, we know the
        # array is not sorted and this return false
        rotation = 0
        for i in range (0,n):
            if nums[i] > nums[(i+1)%n]:
                rotation += 1
            if rotation > 1:
                return False
        return True

my_list = [6,8,9,4,5,7]
x = solution()
print(x.check(my_list))