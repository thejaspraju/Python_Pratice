"""
TC -> O(sqrt(n)) where n is the number
SC -> O(1)
"""
from math import sqrt

def checkPrime(n :int) -> int:
    if n ==1 :
        return False
    for i in range (2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(checkPrime(2))
print(checkPrime(3))
print(checkPrime(10))
