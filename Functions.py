#a=9
#b=8
#c=sum((a,b))  #build in function
def function1(a,b):
    print("You are in function 1",a+b)
def function2(a,b):
    """This will calculate avg of two nos
    doesnt work for 3 nos """
    average = (a+b)/2
    #print(average)
    return average
#v=function2(5,7)
print(function2.__doc__)

