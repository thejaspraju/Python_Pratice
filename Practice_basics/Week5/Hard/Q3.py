"""
Write a Python program to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters.
Input: pyTHon
Output: PYTHON
Input: helLo
Output: helLo
"""

def convertToUppercase(string : str):
    count = 0
    for char in string[:4]:
        if char.isupper():
            count += 1
    if count >=2:
        return string.upper()
    return string

result = convertToUppercase("HelLo")
print(result)

result = convertToUppercase("Helo")
print(result)
