"""
Create a function named arrangeChars which takes a string as a
parameter. Now return a string with max frequency chars at start.
"""
def arrangechar(string:str) -> str:
    character_count = {}
    for ch in string:
        character_count[ch] = character_count.get(ch,0)+1
    character_count = dict(sorted(character_count.items(),key = lambda x:x[1],reverse=True))
    result = ""

    for char, count in character_count.items():
        result += char * count
    return result

print(arrangechar("hellllllllllllllloooooooooooooooo"))