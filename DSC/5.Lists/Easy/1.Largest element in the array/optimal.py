def largest_num(arr:[]):
    n = len(arr)
    maxi = arr[0]
    for i in range (0,n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi

my_list = [54,75,3,90,21,4,2]
print(largest_num(my_list))