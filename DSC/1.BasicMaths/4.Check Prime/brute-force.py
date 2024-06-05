"""
TC -> O(n) where n is the number
SC -> O(1)
"""

def CheckPrime(num:int)-> int:
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(CheckPrime(2))
print(CheckPrime(3))
print(CheckPrime(10))