print("Enter 1st no")
num1=input()
print("Enter 2nd no")
num2=input()
try:
    print("The sum of these two nos",int(num1)+int(num2))
except Exception as e:
    print(e)

    print("This line is important")