# -*-coding:Latin-1 -*

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
        self._adress = "City 16 Avril 1940"

    def _get_adress(self):
        """Method that will called when you need to read the adress"""
        return self._adress

    def _set_adress(self, new_adress):
        """Method will called when you want set the adress"""
        self._adress = new_adress

    def __str__(self):
        """Print Something beautiful"""
        return "Hello World !!"

    def __getattr__(self, item):
        return self.adress
    adress = property(_get_adress, _set_adress)

person = Person("AIT AKKACHE", "Soufiane")
print(person.first_name)
print(person.last_name)
print(person.age)
print(person.adress)
person.adress = "Paris"
ati = "soufiane"
print(person.soufiane)