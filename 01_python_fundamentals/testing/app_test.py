# Import functions from the app
from lib.app import pet_birthday

def test_pet_birthday():
    """Retruns a string wishing the pet a happy birthday"""
    assert pet_birthday(5) == "Happy Birthday! Your pet is now 6"


#create tests that will test the functions