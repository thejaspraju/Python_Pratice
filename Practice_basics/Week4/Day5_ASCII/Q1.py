"""
 Write a function in Python that counts the number of digits in a given
string using ASCII codes.
"""
def count_num(input_string : str)-> int:
    count = 0
    for char in input_string:
        if ord("0") <= ord(char) <= ord("9"):
            count += 1
    return count

print(count_num("Room 1001"))

