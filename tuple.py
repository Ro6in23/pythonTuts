# tup=(1,376,43,787,98,"green",True)
# print(type(tup),tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# print(tup[5])

# tup2=tup[1:4]
# print(tup2)

#Operatiuons on tuples

# countries = ("Spain","Italy","England","India","Germany")
# temp=list(countries)
# temp.append("Russia")  #add item
# temp.pop(3)            #remove item
# temp[2]="Finland"      #Change item
# countries=tuple(temp)
# print(countries)

tuple1=(0,1,2,3,7,31,8,2,3,5)
# res=tuple1.count(3)
# res=tuple1.index(3,4,9)
res=len(tuple1)
print("index  of '3'is:", res)