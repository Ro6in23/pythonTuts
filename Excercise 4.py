# Exercise 4
# Pattern Printing
# Input = Integer n (no of rows)
# Boolean = True or False
# True n=4
# *
# **
# ***
# ****
# False n=4
# ****
# ***
# **
# *

print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()




