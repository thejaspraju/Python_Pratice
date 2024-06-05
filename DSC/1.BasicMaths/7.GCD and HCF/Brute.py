def calcGCD(n:int, m: int) -> int:
    result = []
    if n > m:
        num = n
    else:
        num = m
    for i in range (1, num+1):
        if (n % i == 0) and (m % i == 0):
            result.append(i)
    return max(result)

print(calcGCD(3,9))