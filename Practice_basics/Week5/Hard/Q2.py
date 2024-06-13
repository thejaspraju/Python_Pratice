"""
Write a program to rotate the characters in a string by a given number
of positions. For example, given the input "abcdef" and rotation of 2, the
output should be "efabcd".

Ask string and rotation from the user.

"""
def rotationOfString(string : str, rotation :int)->str:
    for _ in range(rotation):
        string = string[-1] + string[:-1]
    return string

s = "abcdef"
result = rotationOfString(s, 2)

print(result)
