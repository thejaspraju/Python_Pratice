"""
Write a Python program that computes the sum of the ASCII values of
all characters in a string.
"""
def sum_ascii_value(input_string:str) -> int:
    count = 0
    for char in input_string:
        count += ord(char)
    return count

print(sum_ascii_value("Thejaswi"))

#Methiod 2
def sum_ascii_value(input_string:str) -> int:
    return sum(ord(char) for char in input_string) 

print(sum_ascii_value("Thejaswi"))