class Person:
    def __init__(self, name, age):
        self.name = name
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")


pavan = Person("Pavan", -26)
print(pavan.age)
pavan.age = -10
print(pavan.age)

