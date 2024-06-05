"""
Time complexity -> O(log n)
n is number of elements in nums

Space complexity -> O(1)
"""


from typing import List

def lowerbound(num : List,target:int)->int:
    n = len(num)
    low = 0
    high = n-1
    lb= n
    while(low<=high):
        mid = (low+high) // 2
        if num[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid + 1
    return lb

my_list = [1,2,4,4,4,4,4,4,4,4,8,9,9,10]
print(lowerbound(my_list,4))