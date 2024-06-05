"""
 Write a function in Python that removes all numeric characters from a
string by checking their ASCII codes.
"""
def remove_numeric(input_string:str)->str:
    result = ""
    for char in input_string:
        if not (ord("0") <= ord(char) <= ord("9")):
            result += char
    return result

print(remove_numeric("thejas71praju"))

#Medthod 2
def remove_numeric1(input_string:str)->str:
    remove_char = [char for char in input_string if not (ord("0") <= ord(char) <= ord("9")) ]
    return "".join(remove_char)

print(remove_numeric1("thejas71praju"))