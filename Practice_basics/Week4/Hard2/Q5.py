"""
Write a Python code to find the occurrence of each element in a list 
and print the element with the highest occurrence.
"""
my_list = ["Anirudh", 1, 1, 1, 2, 3, 154, 65, 2, 2, 1, 44, 5, 154, 154, "Anirudh"]

unique_elements = []

for i in my_list:
    if i not in unique_elements:
        unique_elements.append(i)

print(unique_elements)
highest_freq = 0
highest_freq_element = 0

for i in unique_elements:
    freq = my_list.count(i)
    print(f"{i} occurs {freq} times")
    if freq > highest_freq:
        highest_freq = freq
        highest_freq_element = i

print(f"Highest frequency = {highest_freq}")
print(f"Highest frequency element = {highest_freq_element}")