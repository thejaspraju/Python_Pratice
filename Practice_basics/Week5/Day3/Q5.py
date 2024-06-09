"""
Create a Python function to sort a dictionary by its values. And return
that new dictionary
"""

from typing import Dict

def sortdict(my_dict : Dict)->Dict:
    return dict(sorted(my_dict.items(),key = lambda x:x[1]))

mydict = {"M1": 89, "M2": 56, "M3": 39}
print(sortdict(mydict))