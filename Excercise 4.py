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
    for i in range(1,one+1):  #for(i=1;i<n+1;i++)
        for j in range(1,i+1): #for(j=1;j<i+1;j++)
            print("*",end=" ")
        print()
elif new ==False:
  for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()

# n=int(input("Enter  no of rows "))
# b=int(input("Enter 1 or 0 "))
# if (b==1):
#     count=0
#     while(count<=n):
#         print("*" * count,end=" ")
#         print()
#         count=count+1
#     elif (b==0):
#     count=n
#     while (count!=0):
#         print("*" * count,end=" ")
#         print()
#         count=count-1
#     else:
#         print("Invalid statement")




