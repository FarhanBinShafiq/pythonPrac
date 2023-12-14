#dict cration
thisDict={
    "name":"Farhan",
    "place":"Tongi",
    "year":1995,
    "university":"NSU"
}

print(type(thisDict))
print(thisDict['year'])
print(len(thisDict))

#Accessing the dict


x=thisDict["university"]
print(x)
#get
y=thisDict.get("university")
print(y)
#keys
r=thisDict.keys()
print(r)
#update the key 7 vVALUES
thisDict['office']='Arced'
print(r)

#VALUES
v=thisDict.values()
print(v)

#items---- method will return the  dict-(keys & value) as a list pr tuple

print(thisDict.items())

#if/else

if "year" in thisDict:
    print("Farhan's DOB  is :",thisDict["year"])

########### add items in the dict


thisDict.update({"year":2005})
print(thisDict)

thisDict['name']='MOye moye'
print(thisDict)

""""
#Remove Items
thisDict.pop('year')
print("Pop remove the year",thisDict)

thisDict.popitem()
print('pop item',thisDict)


thisDict.clear()
print('Clear Method :',thisDict)

"""


################loops########################################

#KEYS

for x in thisDict:
    print("Key :",x)

for x in thisDict.keys():
    print("Keys find my keys method :", x)


#values

for x in thisDict:
    print("Key :",thisDict[x])

for x in thisDict.values():
    print("Keys find my values method :", x)


#key & Value

for x,y in thisDict.items():
    print(x,y)


######################copy###############################

dict2=thisDict.copy()
print('Copy Method :',dict2)

dict3=dict(thisDict)
print("dict method",dict3)



################### nested Loops ##########################






