"""
Make your own list of numbers. Ask a start and end position from User.
Make another different list which will contain number from start to end
position. Use slicing logic
"""
from typing import List

def listSlice(lst:List,start:int,end:int):
    print(lst[start:end+1])

my_list = ["Anirudh", 6, 4, 110.654, True, -54]
listSlice(my_list, 2, 4)