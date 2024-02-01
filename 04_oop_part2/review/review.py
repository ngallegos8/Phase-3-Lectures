# Create a class
class Bird:
    all_birds = []

    def __init__(self, size, species, color, habitat, name=None):
        self.size = size
        self._species = species
        self.color = color
        self.habitat = habitat
        self.name = name
        Bird.all_birds.append(self)

    @property
    def get_color(self):
        return self.get_color
    
    @get_color.setter
    def set_color(self, new_color):
        available_colors = ["Red", "Blue", "White", "Green", "Black"]
        if new_color in available_colors:
            self._color = new_color
        else:
            raise ValueError("Not a valid color!")
        
    @property
    def get_species(self):
        return self._species
    
    @get_species.setter
    def set_species(self, new_species):
        raise Exception("Cannot Change Species")
    
    def migrate(self, new_habitat):
        print(f"Migrating to {new_habitat}")
        self.habitat = new_habitat

    # class methods
    @classmethod
    def find_species(cls, find_species):
        new_list = []
        for bird in Bird.all_birds:
            if bird.get_species == find_species:
                new_list.append(bird)
            return new_list
            # OR ...
            # return [bird for bird in Bird.all_birds if bird._species == find species] #list comprehension version
        
crow = Bird(size="small", species="Crow", color="black", habitat="Urban", name="Scare Crow")
print(id(crow))
print(type(crow))
crow.migrate("City")
print(crow.habitat)
print(crow.name)
print(crow.color)
print(crow.all_birds)
print(Bird.all_birds)
print(Bird.find_species("Crow"))




# Create a method
# Global variables
# Properties, we can do any checks in here!!
# Decorators

# Review property underscore

#Create python environments