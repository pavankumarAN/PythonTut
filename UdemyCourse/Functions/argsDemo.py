def addMany(*nums):
    total = 0;
    for num in nums:
        total += num
    return total


print(addMany(1,2,3,2,3,4,32,42,3,2,2,3,43,4,24,32,4234,23,4,3,2,2,3))
print(addMany(1,2,3,4,5,6))