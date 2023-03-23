a="!!!Robin !!! !!!!Robin"                 #Strings are IMMUTABLE
print(len(a))
print(a)
print(a.upper())          # gives us a new string
print(a.lower( ))
print(a.rstrip("!"))
""" rstrip() helps to strip specific characters attached to the back of the string the '!'on the front doesn't strips """
print(a.replace("Robin","John"))
print(a.split(" ")) # Creates a list
blogheading ="introduction tO pythoN"
print(blogheading.capitalize())
# helps to turn 1st character of the string to Uppercase and also converts all characters to lowercase
b = "Welcome to Earth!!!"
print(b.center(50)) # leaves 50 spaces before the string
print(len(b))
print(len(b.center(50)))
print(a.count("Robin")) # helps to count the occurances of the string
print(b.endswith("!!!")) # gives us boolean data type
str1 = "He's name is Robin. He is an honest man "
print(str1.find("is")) # finds the occurance of "is" wont interpret He's
print(str1.find("ishhh"))#find retrurns -1
#print(str1.index("ishhh"))# gives error
b = "WelcometoEarth"
print(b.isalnum())# Alphanumeric chars:A-Z,0-9,a-z #returns boolean value
c="Welcome00"
print(c.isalpha())#A-Z,a-z # nos are not considered
print(c.islower())
d="Overloaded\n"
print(d.isprintable())# checks whether charactewrs are printable or not
d="World Health Organisation"
print(d.istitle()) # 1st character is uppercase
print(d.swapcase())#upper to lower and lower to upper
