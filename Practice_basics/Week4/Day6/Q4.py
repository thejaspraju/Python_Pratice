"""
Ask 5 integers from user. Then ask a single character from user. Print
those integers separated by that character entered by user
"""

char = input("Enter a character :")
lst = []
for i in range(5):
    lst.append(int(input("enter the number : ")))

result = char.join(str(i) for i in lst)
print(result)

################ Method 2
from typing import List

def joinNumbers(numbers: List[int], char: str) -> str:
    return char.join(str(i) for i in numbers)

numbers = []
for i in range(1, 6):
    num = int(input(f"Enter number {i} = "))
    numbers.append(num)

c = input("Enter a character = ")

result = joinNumbers(numbers, c)
print(result)
