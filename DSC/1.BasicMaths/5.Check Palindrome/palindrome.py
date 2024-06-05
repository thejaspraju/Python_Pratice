def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev_num = 0
        while num > 0:
            ld = num % 10
            rev_num = (rev_num *10) + ld
            num = num // 10
        return rev_num == x

print(isPalindrome(121))