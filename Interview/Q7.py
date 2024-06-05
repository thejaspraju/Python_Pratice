"""
Pythagorean Triplet in an array
arr = [3,4,5]

where a^2 + b^2 = C^2
(3*3) + (4*4) = (5*5)
"""
def checktriplet(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i]**2
    arr.sort()

    for i in range(n-1 , 1,-1):
        s = set()
        for j in range(i-1 , -1 ,-1):
            if (arr[i] - arr[j] )in s:
                return True
            s.add(arr[j])
    return False

arr = [3, 2, 4, 6, 5]
print(checktriplet(arr))