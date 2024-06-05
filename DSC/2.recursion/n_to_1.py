# print 1 to N with out using i+1 and use i-1
list_rev = []
def func(i):
    
    if i < 1:
        return
    list_rev.append(i)
    func(i-1)
    return list_rev
    
print(func(5))