class Person:
    def food(self, item):
        print(f"This person eats {item} as food")
        print("eating food")



class Pavan(Person):
    pass

pavan = Pavan()
pavan.food("Chicken")
# print(Pavan.food("Puliyogare"))