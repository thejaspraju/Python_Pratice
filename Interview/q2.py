"""
Given a positive integer num, write a function that returns True if num is a perfect square else False.
"""
def valid_square(num):
    square = int(num**0.5)
    check = square**2==num
    return check

print(valid_square(10))

print(valid_square(36))
