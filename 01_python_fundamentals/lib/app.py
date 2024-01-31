#!/usr/bin/env python3
import numpy as np
import ipdb

#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
print("Hello World!")

#Pipenv - package and virtual environment tool, uses a pipfile and pipfile.lock, think of node npm
#Use pipenv install to generate a Pipfile and Pipfile.lock
#This will create a virtual environment using the packages in your pipfile and pipfile lock
#Genereate virtual enviroment with 'pipenv shell'
#Exit your virtual environment with 'exit' or 'pipenv --rm'

#Python Package Index
#To install packages to your computer use 'pip install package_name'
#To install packages to your virtual environment use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 
new_array = np.arange(16)
print(new_array)

#Debugging
#To enable ipdb debugging, import ipdb
#ipdb.set_trace() will set a breakpoint
# You can also use the python shell & print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell & print statements
#new 
# def buggy_function(x, y):
#     result = x/y
#     return result

# ipdb.set_trace()
# result = buggy_function(10, 0)
# print("Result: ", result)

#Functions
def method():
    print("Inside the method function")
    def nestedMethod():
        print("In the nested method")
    nestedMethod()

method()



#multiply method
def multiply(a,b):
    return a * b

print(multiply(10,20))

#addition method
def addition(a,b):
    return a + b

print(addition(10, 20))



#Variables
#Todo 5: Create a variable and assign it to a value
pet_name = "Tracker"
pet_name_2 = "Buster"


#Python Data Types
#Todo 6: Create a data type variable

#str
string_var = "this is a string"
print(string_var)

string_var2 = str("this created a string from a str command")
print(string_var2)

#int
number = 100
print(number)

number2 = int(20)
print(number2)

#float
floating_num = 20.6
print(floating_num)

floating_num2 = float(20.5)
print(floating_num2)

#bool
truthy = True
print(truthy)

falsey = False
print(falsey)

#None
null = None
print(null)

#Tuple - Cannot change once it is assigned
my_tuple = (1, "my tuple", [10, 20, 30, 40])
# print(my_tuple + [50, 60, 70])
print(my_tuple)


#Set - Unordered, unchangeable, does not allow duplicates
new_fruit_set = {"apple", "banana", "cherry", "apple"}
print(new_fruit_set)

#Dictionary
car_dictionary = {
    "make": "Polestar",
    "model": "S",
    "year": 2022,
    "colors": ["black", "blue", "grey"]
}
print (car_dictionary)
print(car_dictionary["colors"])
print(car_dictionary.get("year"))
car_dictionary["location"] = "Denver"
print(car_dictionary)
print(car_dictionary["colors"][1])

truck_dictionary = dict(make="Tesla", model="Cyber Truck", year="2024", color="grey")
print(truck_dictionary)
print(truck_dictionary.get("color"))

#lists
new_list = [1,2,3,4,5,6,7,8,9,10]
new_list.append(11)
new_list.remove(1)
new_list.insert(12,13)
print(new_list)
new_list[:0] = [1]
print(new_list)
print(new_list[-1])
print(len(new_list))
print(len(car_dictionary))


#Type Conversion
#Todo 7: Perform type conversion on a data type
age = 28
str_age = str(age)
print(type(str_age))

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true

string = "This is a string"
if type(string) is str:
    print("It's a string")

#if/else syntax
#if condition:
#else:

if "year" in car_dictionary:
    print("year is in description")
else:
    print("Not in the dictionary")

if "wheel" in car_dictionary:
    print("year is in description")
else:
    print("Not in the dictionary")


#if/elif/else syntax
#if condition:
#elif:
#elif:
#else:

# If is True
if 1 in new_list:
    print("1 exists")
elif 4 in new_list:
    print("4 exists")
else:
    print("Does not exist")

# elif is True
if 33 in new_list:
    print("1 exists")
elif 4 in new_list:
    print("4 exists")
else:
    print("Does not exist")

# else is True (If & elif are False)
if 33 in new_list:
    print("1 exists")
elif 87 in new_list:
    print("4 exists")
else:
    print("Does not exist")

x=4
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

if x > 0:
    print("X is positive")
elif x < 0:
    print("X is negative")
# elif x == 0:
#     print("X is 0")
else:
    print("X is zero")



#Syntax of a ternary
#[option1] if [condition] else [option2]

message = "even" if x % 2 == 0 else "odd"
print("x is {message}")
print("x is", message)  #ncatenation example

#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

#Logical Operators
#and, or, not

#Conditionals and Control Flow

#Test if a number is positive
if age > 0:
    print("Positive")

#Test if a string is empty
string=""
if not string:
    print("Empty")

arr = []
if arr is []:
    print("Empty array")


#Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "Tracker"
pet_mood = "Hungry"

#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"
if pet_mood == "Hungry":
    print(f"{pet_name} needs to be fed")
elif pet_mood == "Whinny":
    print(f"{pet_name} needs a walk")
else:
    print(f"{pet_name} is all good")

# terenary version
print(f"{pet_name} needs to be fed") if pet_mood == "Hungry" else print(f"{pet_name} needs a walk") if pet_mood == "Whinny" else print(f"{pet_name} is all good")


#While Loop
count = 0
while count <= 100:
    print(count)
    count += 1


#For Loop and Range
fruits = ["Apple", "Orange", "Mango"]
for fruit in fruits:
    print(fruit)

for num in range(len(new_list)):
    print(num)


#List Comprehension
newList = [num for num in range(10) if num < 5]
print(newList)

#String Interpolation example
name = "programmers"
language = "Python"
print(f"Hello {name} this is {language}")


#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
def pet_status(name, mood):
    print(f"{name} is {mood}")
    mood="Whinny"
    print(f"{name} is now {mood}")
pet_status(pet_name, pet_mood)

    
#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(current_age):
    try:
        return "Happy Birthday! Your pet is now " + str(current_age + 1)

    except TypeError:
        return "Wrong Type"

print(pet_birthday(3))
print(pet_birthday("3"))
