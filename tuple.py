
######## Convert the tuple into the list
newTuple=(1,2,3,4,5,6,7,8)

#convert into list

a=list(newTuple)
print(type(a))


a.append(9)
print(a)

#convert into tuple

b=tuple(a)

print(type(b))
print(b)



#########adding two tuple 

x=(9,10,11,12)

newTuple +=x
print(newTuple)