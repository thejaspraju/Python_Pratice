"""
Ask a string from user. Replace all the space characters with “-”. 
Do not use replace() method.
"""

def replaceSpace(string):
    result = ""
    for chr in string:
        if chr == " ":
            result += "-"
        else:
            result += chr
    return result

input_string = input(" enter the string :")
result = replaceSpace(input_string)
print(result)