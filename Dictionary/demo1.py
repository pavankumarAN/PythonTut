user_details = {
    "name" : "Pavan",
    "age" : 25,
    "height" : 5.6,
    "weight" : 70,
    "blood_group" : "B+",
    "isEmployed" : True,
    "address" : "Koramangala, Bengaluru"
}
#
# print(user_details.keys())
for k in user_details.keys():
    print(k)

for v in user_details.values():
    print(v)

for i in user_details.items():
    print(i)