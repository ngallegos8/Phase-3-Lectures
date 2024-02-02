# One to One
#Create a one to one relationship between apartments and tennets
#Apartments should be initialized with name, location, and a tenet that is set to none
#Create Methods get_tenent that gets the tenent, and set_tenent to set a new tenent
class Apartment:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.tenet = None
    
    def get_tenet(self):
        return self._tenet
    
    def set_tenet(self, new_tenet):
        if type(new_tenet) is Tenet:
        # if isinstance(new_tenet, Tenet):
            if self._tenet is not None:
                self._tenet.apartment = None
                new_tenet.apartment = self
                self._tenet = new_tenet
            else:
                self._tenet = None

class Tenet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.apartment = None

david = Tenet("David", 27)
sunnyside = Apartment("Sunnyside", "Denver")
david.apartment = sunnyside
sunnyside.tenet = david
print(david.apartment)
print(sunnyside.tenet)


#One to Many
#Create a one to many relationship between a Team and Player
#Team should be initialized with a name, mascot, and have an attrivute players that is a list
#Player should be initilized with a name
#Create a method add_player to add a player to the players list

class Team:
    def __init__(self, name, mascot):
        self.name = name
        self.mascot = mascot
        self.players = []

    def add_player(self, new_player):
        if isinstance(new_player, Player):
            print(new_player.team)
            self.players.append(new_player)
            new_player.team = self
        else:
            raise Exception("Must be a Player")

class Player:
    player_list = []
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.team = None
        Player.player_list.append(name)

player1 = Player("Guy", "Bank Teller")
player2 = Player("Other Guy", "Security")
team1 = Team("Free Guy", "Bear")

team1.add_player(player1)
print(player1.team.name)


#Many to Many
#Create a many to many relation ship between a teacher and student
#Teacher should be initialized with name, subject, and have a list of students
#Student should be initialized with a name, grade, and have a list of teachers

class Teacher:
    students = []
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []
        Teacher.students.append(self)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.teachers = []



