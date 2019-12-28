# x = [1,2,"Pavan", 15.6]
# x.insert(2,5)
# print(x)

li = [1,2,3,4,5]
squa = [num*num for num in li]
print(squa)
even = [ num*2 if num%2==0 else num/2 for num in li]
print(even)