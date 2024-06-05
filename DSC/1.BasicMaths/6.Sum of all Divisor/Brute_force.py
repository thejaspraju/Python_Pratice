def sumOfAllDivisor(n:int) -> int:
    sum = 0
    for i in range(1,n+1):
        for j in range (1 , i+1):
            if i % j == 0:
                sum += j
    return sum

print(sumOfAllDivisor(5))