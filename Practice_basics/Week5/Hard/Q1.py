"""
Given a list of strings, concatenate them into a single string separated
by spaces. For example, given the input ["Hello", "World", "Python"], the
output should be "Hello World Python".

Make a list on your own.
Don’t use the JOIN function.
"""
str_list = ["Hello","World","Python"]
output = ""
for char in str_list:
    output +=char + " "

print(output)

####### Method 2

from typing import List

def joinwords (words : List[str]) -> str:
    result = ""
    for word in words:
        result += word +" "
    return result

my_words = ["Hello", "World", "Python"]

s = joinwords(my_words)
print(s)

