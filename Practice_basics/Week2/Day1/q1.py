"""
Q1. Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.
"""
def max(a,b,c):
    if a > b and a > c :
        return a
    elif c > a and c >b:
        return c
    else:
        return b

def min(a,b,c):
     if a < b and a < c :
        return a
     elif c < a and c < b:
        return c
     else:
        return b


print(max(1,2,3))
print(min(1,2,3))

###################################

def maxi(a: float, b: float, c: float):
    result = max(a, b, c)
    print(f"{result} is the max number")


def mini(a: float, b: float, c: float):
    result = min(a, b, c)
    print(f"{result} is the min number")


num1: float = 10
num2: float = 5
num3: float = 8

maxi(num1, num2, num3)
mini(num1, num2, num3)

