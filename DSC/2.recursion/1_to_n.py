# print 1 to N with out using i+1 and use i-1
def func(i):
    if i < 1:
        return
    func(i-1)
    print(i)
func(5)