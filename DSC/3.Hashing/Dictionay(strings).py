string = "aeroplllanneee"

hash_map = {}

# Pre compute or pre storing

for num in string :
    hash_map[num] = hash_map.get(num,0) + 1

print(hash_map)

number = input("Enter char to count = ")
print(hash_map.get(number,0))