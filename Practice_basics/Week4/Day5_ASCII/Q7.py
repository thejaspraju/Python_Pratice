"""
Implement a Python function that checks if a string contains any
special characters (non-alphanumeric) by using ASCII codes.
"""
def check_special_characters(input_string:str) -> bool:
    for char in input_string:
        if not((ord("a")) <= ord(char.lower()) <= ord("z") or
        ord ("0") <= ord(char) <= ord("9")):
            return True
    return False

print(check_special_characters("password123!"))