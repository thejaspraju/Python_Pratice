
def reversearry(arr):
    n = len(arr)
    i=0
    j=n-1
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr
    
my_lst = [1,2,3,4,5,6]
print(reversearry(my_lst))