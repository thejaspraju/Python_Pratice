"""
Write a Python function that takes a dictionary as input where the
values are lists of integers. The function should return a new dictionary
where the values are lists containing only the even integers from the
original lists
"""

from typing import Dict

def check_even_value(my_dict : Dict)->Dict:
    for key,value in my_dict.items():
        result = []
        for i in value:
            if i % 2 == 0:
                result.append(i)
        my_dict[key] = result
    return my_dict

input_dict = {"a": [1, 2, 3, 4, 5], "b": [10, 11, 12, 13, 14]}
filtered_dict = check_even_value(input_dict)
print(filtered_dict)
