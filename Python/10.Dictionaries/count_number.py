arr = [1,4,5,5,4,6,3,1,1,1,1,2,9]
n = len(arr)
fre_map = dict()

for i in range(n):
    fre_map[arr[i]] = fre_map.get(arr[i],0) + 1

'''

for i in range(n):
    if arr[i] in fre_map:
        fre_map[arr[i]] = fre_map[arr[i]] + 1
    else:
        fre_map[arr[i]] = 1
'''
print(fre_map)