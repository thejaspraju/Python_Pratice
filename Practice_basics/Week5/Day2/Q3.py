"""
 Write a function that updates the values of a dictionary by multiplying
them by a given factor only if the value is an integer.
"""

def update_factor(my_dict,k):
    for key,value in my_dict.items():
        if type(value) == int:
            my_dict[key] = value * k
    return my_dict

ans = update_factor({"apple": "9", "banana": 8, "cherry": 7, "orange": 10}, 3)
print(ans)


