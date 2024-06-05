"""
Bubble sort
Time complexity - O(n^2) (Average and worst)
Time complexity - O(n) (Best case)
Space complexity - O(1)
"""
def bubble_sort(arr):
    n = len (arr)
    for i in range (n-2,-1,-1):
        for j in range (0 , i+1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [5,3,9,1,8,4,2]
print(bubble_sort(arr))