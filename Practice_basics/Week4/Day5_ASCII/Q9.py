"""
 Develop a Python program that finds the character with the maximum
ASCII value in a given string.
"""
def check_maxi(input_string):
    max_char = ""
    maxi_ascii = 0
    for char in input_string:
        char_ascii = ord(char)
        if char_ascii > maxi_ascii:
            max_char = char
            maxi_ascii = char_ascii
    return max_char

print(check_maxi("Thejaswi"))


#Method 2
def check_maxi1(input_string):
    max_char = max(input_string,key = lambda x:ord(x))
    return max_char

print(check_maxi1("Thejaswi"))