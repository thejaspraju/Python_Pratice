for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

"""
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5
"""
for i in range(5,0,-1):
    for j in range(1,i):
        print(" ", end=" ")
    for k in range(i, 6):
        print(k, end=" ")
    print()