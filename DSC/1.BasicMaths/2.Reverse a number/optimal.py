"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""

def reverseNumber(num:int)-> int:
    n = num
    reversed_num = 0
    while n > 0:
        last_digit = n%10
        reversed_num = (reversed_num *10) + last_digit
        n = n//10
    return reversed_num

print(reverseNumber(1234))