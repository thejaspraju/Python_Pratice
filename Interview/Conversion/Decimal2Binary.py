"""
Input : 7                                                         
Output :111
"""
def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    
    return (num % 2)

print(DecimalToBinary(7))
print(DecimalToBinary(14))
print(DecimalToBinary(10))