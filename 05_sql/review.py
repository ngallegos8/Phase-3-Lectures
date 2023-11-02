# One to One
#Create a one to one relationship between apartments and tennets
#Apartments should be initialized with name, location, and a tenet that is set to none
#Create Methods get_tenent that gets the tenent, and set_tenent to set a new tenent

class Apartment:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.tenant = None

    @property
    def get_tenet(self):
        return self._tenant
    
    @get_tenet.setter
    def set_tenet(self, new_tenant):
        if isinstance(new_tenant, Tenant):
            new_tenant.apartment = self
            self._tenant = new_tenant
        else:
            self._tenant = None 
class Tenant:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.apartment = None

david = Tenant("David", 25)
sunnyside = Apartment("Sunnyside", "Location")
sunnyside.tenant = david 

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

    def add_players(self, new_player):
        self.players.append(new_player)
        new_player.team = self

class Player:
    def __init__(self, name):
        self.name = name
        self.team = None

player1 = Player("Dylan")
player2 = Player("Buffy")
team1 = Team("Good team 1", "Dogs")
team2 = Team("Good team 2", "Dogs")
team1.add_players(player1)
team1.add_players(player2)
team2.add_players(player1)
print(team1.players)
print(player1.team)
print(team2.players)
print(team1.players)
print(player1.team.name)

#Many to Many
#Create a many to many relation ship between a teacher and student
#Teacher should be initialized with name, subject, and have a list of students
#Student should be initialized with a name, grade, and have a list of teachers
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.teachers.append(self)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.students.append(self)

teacher1 = Teacher("David", "Phase 1")
teacher2 = Teacher("Stephen", "Phase 3")

student1 = Student("Buffy", "Python")
student2 = Student("George", "Python")

teacher1.add_student(student1)
teacher1.add_student(student2)

student2.add_teacher(teacher1)
student1.add_teacher(teacher1)

# print(teacher1.students)
for student_name in teacher1.students:
    print(student_name.name)
# print(student1.teachers.subject)


