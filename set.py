newSet={'A','B','C','D','E'}


#ACCESS ON SET

for x in newSet:
    print('Access on set')
    print(x)

#Add data set

print("add new data")
newSet.add('F')
print(newSet)

#add two set

a={1,2,3,4,5,6}
newSet.update(a)
print('add two set')
print(newSet)


#remove

a.remove(3)
print('Remove :',a)