#Function Way
def factorial(n):
    if n ==0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(3))

# Parameterized way
def factorial(i ,sum):
    if i < 1:
        print(sum)
        return
    factorial(i-1,sum*i)

factorial(3,1)