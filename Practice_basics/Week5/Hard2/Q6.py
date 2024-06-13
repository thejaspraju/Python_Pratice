"""
. Write a Python program to generate two strings from a given string. For
the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.
Input: aabbcceffgh
Output
string1 = egh
string2 = abcf
"""
from typing import List
def oddCharacters(string:str):
    character_count = {}
    for ch in string:
        character_count [ch] = character_count.get(ch,0) + 1
    str1 = str2 = ""
    for char,count in character_count.items():
        if count > 1:
            str1 += char
        else:
            str2 += char
    print(str1)
    print(str2)

oddCharacters("aabbcceffgh")