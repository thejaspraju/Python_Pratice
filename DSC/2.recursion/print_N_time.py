"""
Print name N times

TC -> O(N)
SC -> O(N)
"""



def func(i,n):
    if i > n:
        return 
    print("Code & Debug")
    func(i+1 , n)
func(1,4)