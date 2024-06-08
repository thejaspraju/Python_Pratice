"""
Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are squares of the keys
"""

def create_dictionary ():
    return {x : x **2 for x in range(1,16)}

def create_dict2():
    square_dict = {}
    for x in range(1,16):
        square_dict[x] = x**2
    return square_dict


ans = create_dictionary()
print(ans)
ans1 = create_dict2()
print(ans1)
