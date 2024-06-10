"""
Write a function which accepts a String as a parameter and return the
reversed words as a String.
"""

def reversestring(input_string : str):
    return input_string[::-1]

print(reversestring("we are in earth"))

####### Method 2
def reverseWord(string:str)->str:
    words = string.split()
    words.reverse()
    result = " ".join(i for i in words)
    return result

print(reverseWord("python is great"))