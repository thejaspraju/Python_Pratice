from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    mylst = [0] * n
    for x in edges:
        if x > n:
            continue
        mylst[x-1] += 1
    return mylst

print(countFrequency(5,2,[1,2,2,4,2]))