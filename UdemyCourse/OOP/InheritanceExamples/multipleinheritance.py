class Human:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def colorWh(self):
        print(f"looks in Red")

class Manager:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def feature(self):
        print(f"Person with name {self.name} of age {self.age} having skin color {self.color}")

    def colorWh(self):
        print(f"looks in {self.color}")

class Employee(Human,Manager):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


pavan = Employee("Pavan", 26, "white")
print(pavan.name)
pavan.feature()
pavan.colorWh()
