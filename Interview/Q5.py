"""
Remove duplicates from sorted array
"""
def removeduplicates(arr):
    n = len(arr)
    LftIndex = 1
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            arr[LftIndex] = arr[i]
            LftIndex = LftIndex + 1
    return LftIndex

array_1 = [1,2,2,3,3,4]
print(removeduplicates(array_1))


array_2 = [1,1,3,4,5,6,6]
print(removeduplicates(array_2))