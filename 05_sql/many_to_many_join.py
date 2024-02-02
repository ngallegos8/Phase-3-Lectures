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
                print(f"Player: {contract.player.name} Payout: {contract.money}")

class Player:
    all = []

    def __init__(self, name, team):
        self.name = name
        self.team = team
        Player.all.append(self)


class Contract:
    all = []

    def __init__(self, money, length, sponsor):
        self.money = money
        self.length = length
        self.sponsor = sponsor
        self.player = None
        Contract.all.append(self)

    def sign_contract(self, player):
        if isinstance(player, Player):
            self.player = player

    def delete(self):
        del self

nike = Sponsor("Nike", "Clothing")
jordan = Player("Jordan", "Bulls")
nike_contract = Contract("1 Billion", "Forever", nike)

nike_contract.sign_contract(jordan)
nike.get_contracts()

nike_contract.delete()
print(nike_contract.delete())

print(nike_contract)
