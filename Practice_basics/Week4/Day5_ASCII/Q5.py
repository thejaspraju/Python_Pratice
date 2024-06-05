"""
Write a Python script that replaces each non-alphabetic character in a
string with a space, using ASCII to determine character types.
"""
def replace_non_aplha_space(input_string : str) -> str:
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char
        else:
            result += ' '
    return result

print(replace_non_aplha_space( "Hello, World!"))


# Method 2
def replace_non_alphabetic_ascii(input_string: str) -> str:
    replaced_chars = [char if char.isalpha() else " " for char in input_string]
    return "".join(replaced_chars)