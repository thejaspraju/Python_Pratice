"""
Write a program in Python to calculate the average score of each
student across multiple subjects stored in a dictionary of dictionaries.
Student scores:
{
    'John': {'Math': 85,'Science': 90,'English': 80},
    'Alice': {'Math': 75,'Science': 88,'English': 92},
    'Bob': {'Math': 90,'Science': 85,'English': 78}
}
Output:
John: 85.0
Alice: 85.0
Bob: 84.33333333333333

"""
from typing import Dict

def avgscore(my_dict:Dict):
    for key, value in my_dict.items():
        total = 0
        x = len(value)
        for v in value.values():
            total = total+v
        avg = total//x
        print(f"the average of {key} is {avg}")
my_dict = {
    'John': {'Math': 85,'Science': 90,'English': 80},
    'Alice': {'Math': 75,'Science': 88,'English': 92},
    'Bob': {'Math': 90,'Science': 85,'English': 78}
}
avgscore(my_dict)