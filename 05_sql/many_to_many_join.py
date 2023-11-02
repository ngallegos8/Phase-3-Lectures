#Create a many to many relationship with a join for a sponsor, player, and contract object

class Sponsor:
    all = []
    def __init__(self, name, product):
        self.name = name
        self.product = product
        Sponsor.all.append(self)

    def get_contracts(self):
        for contract in Contract.all:
            if contract.sponsor is self:
                print(f"Player: {contract.player.name} Payout: {contract.salary}")
class Player:
    all = []
    def __init__(self, name, team):
        self.name = name
        self.team = team
        Player.all.append(self)

class Contract:
    all = []
    def __init__(self, salary, length, sponsor):
        self.salary = salary
        self.length = length
        self.sponsor = sponsor
        self.player = None
        Contract.all.append(self)
    def sign_contract(self, player):
        self.player = player

    def delete(self):
        del self

nike = Sponsor("Nike", "Clothing")
adidas = Sponsor("Adidas", "Clothing")
buffy = Player("Buffy", "Denver Nuggets")
stephen = Player("Stephen", "Bulls")

nike_contract = Contract(1000000000, "5 Years", nike)
adidas_contract = Contract(1000000, "5 Years", nike)
nike_contract.sign_contract(buffy)
adidas_contract.sign_contract(stephen)
nike.get_contracts()
adidas.get_contracts()

