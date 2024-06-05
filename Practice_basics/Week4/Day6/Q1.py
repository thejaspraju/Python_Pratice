"""
Ask a string from user. If the length of string is odd, then change all the
capital letters to small and vice versa, but if the length of string is even,
reverse the string. Do this using a function and return the output.
"""
def string_operation(input_string:str):
    n = len(input_string)
    if (n%2 == 0):
        return input_string[::-1]
    else:
        return input_string.swapcase()

str_input = input("Enter the string : ")
print(string_operation(str_input))