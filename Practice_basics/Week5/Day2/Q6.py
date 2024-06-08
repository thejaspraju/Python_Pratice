"""
 Ask a string from user. Store the frequency of each character in the
dictionary. Then print the character with the maximum frequency.
"""

from typing import Dict

def check_frequency(string) -> Dict:
    freq = {}
    for char in string:
        if char in freq :
            freq[char] += 1
        else:
            freq[char] = 1
    max_char = None
    max_freq = 0

    for char,count in freq.items():
        if count > max_freq:
            max_freq = count
            max_char = char
    
    print(f"the character with maximum frequenct is : {max_char}")

check_frequency("heeeeeeeeeeeeeeeeeeellllllloo")

        
