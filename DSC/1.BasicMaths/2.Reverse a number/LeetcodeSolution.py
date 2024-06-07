"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""
"""
brute force check your leet code for test cases
"""
class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        is_negative = False
        if x < 0:
            is_negative = True
            # x=x * -1
            x = abs(x)
        while x > 0:
            last_digit = x % 10
            reverse_number = (reverse_number * 10) + last_digit
            x = x // 10
        if is_negative:
            reverse_number = reverse_number * -1
        #This is Leet code condition
        if reverse_number < (-(2**31)) or reverse_number > (2**31 - 1):
            return 0
        return reverse_number
obj = Solution()
print(obj.reverse(3452))

# this is a optimal solution

"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""

def reverseNumberOptimal(num: int) -> int:
    n = num
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = (reversed_number * 10) + last_digit
        n = n // 10
    return reversed_number

print(reverseNumberOptimal(1234))
