"""
 Write a function which accepts a String and another string (which will
be a single character) as a parameter. Join that string along with that
character.
"""
def add_char_string(string:str,char:str):
    words = string.split()
    return char.join(i for i in words)

print(add_char_string("Ths is new","@"))