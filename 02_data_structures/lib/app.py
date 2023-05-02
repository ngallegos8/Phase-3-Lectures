# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Mutable
# Creating Lists
#1. Create a list of 10 pet names

# Reading Information From Lists
#2. Return the first pet name

#3. Return all pet names beginning from the 3rd index

# Inclusive

#4. Return all pet names before the 3rd index

# Exclusive


#5. Return all pet names beginning from the 3rd index and "up to" and (exclusive) the 7th

# Inclusive

# Exclusive

#6. Find the index of a given element => .index()

#7. Reverse the original list => .reverse()

# Mutative (Destructive)
    # Demonstrates the Mutability of Lists

#8. Return the frequency of a given element => .count()

# Updating Lists
#9. Change the first name to all uppercase letters => .upper()

#10. Append a new name to the list => .append()

# Mutative (Destructive)

#11. Add a new name at a specific index => .insert()
# Argument 1 => Index
# Argument 2 => Value

#12. Add two lists together => +

#13. Remove the final element from the list => .pop()
# Mutative (Destructive)

#14. Remove element by specific index => .pop()

#15. Remove a specific element => .remove()

#16. Remove all pet names from the list => .clear()

#Tuple
# Why Are Tuples Immutable?
    # What advantages does this provide for us? In what situations
    # would this serve us?

    # Helps us to preserve our data, keep it from being
    # changed or altered in any way.

# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable

#17. Create a Tuple of 10 pet ages => () 

#18. Print the first pet age => []

# Testing Mutability 
#19. Attempt to remove an element with ".pop" (should error)

# AttributeError: 'tuple' object has no attribute 'pop'

#20. Attempt to change the first element (should error) => []

# Tuple Methods
#21. Return the frequency of a given element => .count()

#22. Return the index of a given element  => .index()

# BREAK PERIOD POINT

#23. Create a Range 
# Note:  Ranges are primarily used in loops

# Sets
#24. Create a set of 3 pet foods

#Mapping Types

# Dictionaries 
# Creating 
#25. Create a dictionary of pet information with the keys "name", "age" and "breed"

# Looks Like...JSON


#26. Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)

    # Main advantage of using "dict" => Less Keystrokes (Less Quotes to Write Into Code)

# Reading
#27. Print the pet attribute of "name" using bracket notation 

    # KeyError: 'temperament'

#28. Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

    # Returns None

# Updating 
#29. Update Trackers's age to 12 => []


#30. Update Brindle's age to 26 => .update({...})


# Deleting
#31. Delete Trackers's age using the "del" keyword => []

#32. Delete Brindles's age using ".pop"

#33. Delete the last item for Tracker using "popitem()"

# Loops 
#create an array of pet_info
pet_info = [
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

pet_info_2 = [
    {
        'name':'Bud',
        'age':5,
        'breed': 'golden retriever',
    }, 
    {
        'name':'Princess Grace',
        'age':9,
        'breed': 'persian',
    },
    {
        'name':'WiFi',
        'age':4,
        'breed': 'wolf',
    }
]

#34. Loop through a range of 10 and print every number within the range

#35. Loop through a range between 50 and 60 that iterates by 2 and print every number

#36. Loop through the "pet_info" list and print every dictionary 

#37. Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_info" as an argument


#38. Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 


#39. Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# List Comprehensions => []
# map like 
#40. Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# find like
#41. Use list comprehension to find a pet named spot

# filter like
#42. Use list comprehension to find all of the pets under 3 years old


# Generator Expression => ()
#43. Create a generator expression matching the filter above

    # Main Benefit => Less Memory Intensive


# Accessing Generator Object Values

# 1. Using next()


# 2. Using a for loop