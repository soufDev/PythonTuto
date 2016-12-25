# -*-coding:Latin-1 -*

class Personne:
    """classe définissant une personne"""

    def __new__(cls, nom, prenom):
        print("Calls the method __new__ of the class {}".format(cls))
        # you let the work to the object
        return object.__new__(cls)

    def __init__(self, nom, prenom):
        """Personne class constructor"""
        print("Calls the method __init__")
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_residence = "Lyon"


def create_person(person, last_name, first_name):
    """Method that takes a constructor Role"""
    person.last_name = last_name
    person.first_name = first_name
    person.age = 21
    person.residance_place = "Lyon"


def present_person(person):
    """Fonction to describe/present person"""
    print("{} {}".format(person.first_name, person.last_name))


# Methods dectionnary
methods = {
    "__init__": create_person,
    "present": present_person,
}

Person = type("Person", (), methods)
john = Person("soufiane", "AIT AKKACHE")
john.present()
print(john.last_name)
print(john.first_name)
print(john.age)
print(john.residance_place)


class MyMetaClass(type):
    """Meta class Example"""

    def __new__(metacls, name, bases, dict):
        """create your class"""
        print("You create class {}".format(name))
        return type.__new__(metacls, name, bases, dict)


class Myclass(metaclass=MyMetaClass):
    pass

