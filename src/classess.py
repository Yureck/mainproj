


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"





class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

        def get_info(self):
            return f"{self.name} is {self.age} years old."
    
    
roger = Dog("Roger", 4)
print(roger.bark())  # Output: Woof!


