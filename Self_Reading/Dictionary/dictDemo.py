thedict = {
    "name" : "Pavankumar AN",
    "age" : 26
}

print(thedict)
print(thedict["name"])
print(thedict.get("name"))

for x in thedict:
    print(thedict[x])

for y in thedict.values():
    print(y)

for key,value in thedict.items():
    print(x,y)

if "name" in thedict:
    print(thedict["name"])


print(len(thedict))
