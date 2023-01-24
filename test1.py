"""
1
2 3
4 5 6
7 8 9 10

k=1
for i in range(1,6):
    for n in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()

1 2 3 4
5 6 7
8 9
10
"""
k=1
for i in range(1,5):
    for n in range(1, 6-i):
        print(k,end=" ")
        k=k+1
    print()
