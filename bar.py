age = input("Enter your age")
if (age):
    if int(age) >= 18 and int(age) < 21:
        print('wristband')
    elif int(age)>21:
        print('drink, normal entry')
    elif int(age)<18:
        print('sorry, too young')
else:
    print("Please enter age")