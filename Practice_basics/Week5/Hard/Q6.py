"""
Write a Python program to convert string values of a given dictionary
into integer/float data types.
Example 1:
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
Output:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
"""
from typing import List

def convertValues(data: List[dict]):
    for d in data:
        for key, value in d.items():
            if "." in value:
                d[key] = float(value)
            else:
                d[key] = int(value)
    return data
list1 = [
    {"x": "10", "y": "20", "z": "30"},
    {"p": "40", "q": "50", "r": "60"},
]

output1 = convertValues(list1)
print(output1)