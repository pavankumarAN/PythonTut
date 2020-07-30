nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")



values = [1,2,3,4,5,6]
if any([i%2==0 for i in values]):
   print("Even numbers")