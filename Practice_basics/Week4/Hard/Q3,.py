"""
Python Program to remove all duplicates from a given string
"""
def remove_duplicates(string:str) -> str:
    result = ""
    for ch in string:
        if ch not in result:
            result+= ch
    return result

string = "hheeelllooo"
print(remove_duplicates(string))