def isPalindrome(x : int)-> bool:
    if x < 0:
        return False
    num = x
    revers_num = 0
    while num > 0:
        revers_num = (revers_num*10) + num % 10
        num = num //10
    return revers_num == x

print(isPalindrome(121))