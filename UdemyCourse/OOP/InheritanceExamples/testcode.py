class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        # Animal.__init__(self, name, species)
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

blue = Cat("Blue", "Kallbekku", "karibekku", "chendu")
print(blue)
