class Cocktails:
    def __init__(self, spirit, oz, name):
        self.spirit = spirit
        self.oz = oz
        self.bars = []
        self.name = name

class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cocktails = []

    def build_menu(self, menu_array):
        for item in menu_array:
            if type(item) is Cocktails:
                self.cocktails.append(item)
                item.bars.append(self)

pony_up = Bar("Pony Up", "Blake St")
beacon = Bar("Beacon", "RiNo")

rum_and_coke = Cocktails("Rum", 5, "Rum and Coke")
tequila_shot = Cocktails("Tequila", 3, "Tequila Shot")

pony_up.build_menu([rum_and_coke, tequila_shot])
print(pony_up.cocktails)

for c in pony_up.cocktails:
    print(f"We offer {c.spirit}")
for c in pony_up.cocktails:
    print(f"We offer {c.name}")

print(rum_and_coke.bars)

for b in rum_and_coke.bars:
    print(f"Find here: {b.name}")

class Test:
    def __init__(self) -> None:
        pass