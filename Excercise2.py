#Excercise 2-Fault calculator
#Design a calculator which will solve all the problems except the following ones:
# 45*3= 555 , 56+9=77 , 56/6 = 4
#Your program should take an operator and the two numbers as input from the user and then return the result
print("Enter first number")
n1=int(input())
print("Enter second number ")
n2=int(input())
print("Choose your operator:+,-,*,/")
n3=input()
if n1==45 and n2==3 and n3=="*":
    print(" 555")
elif n1==56 and n2==9 and n3=="+":
    print("77")
elif n1==56 and n2==6 and n3=="/":
    print(" 4")
elif n3=="+":
    print(n1+n2)
elif n3=="*":
    print(n1*n2)
elif n3=="/":
    print(n1/n2)
elif n3=="-":
    print(n1-n2)
else:
    print("Unexpected error")


