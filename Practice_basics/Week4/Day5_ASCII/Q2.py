"""
 Develop a Python script that counts how many letters are in a string by
checking ASCII values.
"""

def count_char(input_string : str) -> int:
    count = 0
    for char in input_string:
        if ord("a") <= ord(char.lower()) <= ord("z"):
            count += 1
    return count

print(count_char("Thejaswi1993"))