class Person:
    """Class defining Person with
        - Family Name
        - First Name
        - Age
        - place of residence"""

    def __init__(self, last_name, first_name): # our constructor
        self.last_name = last_name
        self.first_name = first_name
        self.age = 25
        self.adress = "City 16 Avril 1940"


person = Person("AIT AKKACHE", "Soufiane")
print(person.first_name)
print(person.last_name)
print(person.age)
print(person.adress)
person.adress = "Paris"
print(person.adress)
print(person)