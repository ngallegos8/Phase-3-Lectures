class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    
    def petAnimal(self):
        print(f"Petting {self.name}")

class Dog(Animal):
    def __init__(self, breed, name, color, age, size):
        super().__init__(name, color, size)
        self.breed = breed
        self.age = age

    def petAnimal(self):
        super().petAnimal()
        print(f"{self.name} is happy")

class Bird(Animal):
    def __init__(self, size, species, color, habitat, name=None):
        super().__init__(name, color, size)
        self.species = species
        self.habitat = habitat


pigeon = Bird("Small", "Pigeon", "Grey", "City", "Pie")
pigeon.petAnimal()
print(pigeon.size)

tracker = Dog("Golden", "Tracker", "Brown", 5, "Large")
print(tracker.size)
print


    