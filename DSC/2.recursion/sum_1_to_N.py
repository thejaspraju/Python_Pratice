# this is Parameterised Way

def func(i,sum):
    if i < 1:
        print(sum)
        return
    func(i-1 , sum+i)

func(10,0)

#This is functional Way
def func1(n):
    if n == 1:
        return 1
    return n + func1(n -1)

print(func1(10))
