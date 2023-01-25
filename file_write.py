# writing and appending
# f = open("robin2.txt","a")
# a = f.write("Robin is a good guy\n")
# print(a)
# f.close()

# handle read and write both
f = open("robin2.txt","r+")
print(f.read())
f.write("Thank you for reading this")
