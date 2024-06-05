"""
Write a function which accepts a String as a parameter and return each
word being in reverse
"""

def reverse_words(string:str):
    result = []
    words = string.split()
    for char in words:
        result.append(char[::-1])
    return result

print(reverse_words("python is great"))

# Method 2
def reverseWords(string: str) -> str:
    words = string.split()
    result = " ".join(i[::-1] for i in words)
    return result

    # Shortcut
    # return " ".join(i[::-1] for i in string.split())


r = reverseWords("python is great")
print(r)
    