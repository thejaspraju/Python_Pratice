"""
Convert Snake case to Pascal case.
Input: python_is_great
Output: PythonIsGreat
"""
def snaketoPascal(string:str):
    word = string.split('_')
    result = ""
    for ch in word:
        result += ch[0].upper()+ch[1:]
    return result

print(snaketoPascal("python_is_great"))

########3 Method 2
test_str = "we_are_learning_python_programming"
res = test_str.replace("_", " ").title().replace(" ", "")
print(res)
