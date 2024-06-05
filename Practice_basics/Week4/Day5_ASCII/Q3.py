"""
 Implement a function in Python to check if a string is alphanumeric by
examining the ASCII values of its characters.
"""
def check_ascii_value(input_string : str) -> bool:
    for char in input_string:
        if not(ord("a") <= ord(char.lower()) <= ord("z") or
               ord("0")<= ord(char) <= ord("9")):
            return False
    return True

print(check_ascii_value("Thejas7176"))
print(check_ascii_value("Ayush 0212"))