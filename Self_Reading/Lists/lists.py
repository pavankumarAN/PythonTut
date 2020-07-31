thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[2:])
print(thislist[-2])
print(thislist[:-3])
print(thislist[:2])
print(thislist[2:5])
print("kiwi" in thislist)

# for name in thislist:
#     print(name + " Index : {}".format(thislist.index(name)))
thislist.append("Baarehannu")
print(thislist)
print(thislist.pop())
thislist.remove("kiwi")
print(thislist)
thislist.insert(2,"Kaarehannu")
print(thislist)

vegetables = ["one", "two", "three"]
thislist.extend(vegetables)
print(thislist)