"""
Create a function named oddCharacters which takes a string as a
parameter. Now return a list of characters which appears odd times in that
string.
"""
from typing import List
def oddCharacters(string:str) -> List:
    character_count = {}
    for ch in string:
        character_count [ch] = character_count.get(ch,0) + 1
    result = []
    for char,count in character_count.items():
        if count % 2 == 1:
            result.append(char)
    return result

print(oddCharacters("aeroplane"))
    