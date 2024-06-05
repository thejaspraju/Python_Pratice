lst = []
list_length = int(input("enter the length = "))
for i in range (list_length):
    num = int(input("Enter number = "))
    lst.append(num)
print(list)

#Pre Comute
hash_lsit = [0] * 13 # [0,0,0,0,......13 times zero]
for num in lst:
    hash_lsit[num]+=1

print(hash_lsit)
n = int(input("Enter number to count = "))
print(hash_lsit[n])     # Fetching