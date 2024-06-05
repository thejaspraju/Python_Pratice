lst = [5, 4, 2, 5, 4, 2, 1, 1, 1, 3, 5, 3]

hash_map = {}

# Pre Storing
for num in lst:
    hash_map[num] = hash_map.get(num,0)+1

print(hash_map)

number = int(input("Enter number to count = "))
print(hash_map.get(number,0))