class Person:
    """Class describs a Person"""

    def __init__(self, last_name):
        """Class constructor"""
        self.last_name = last_name
        self.first_name = "Soufiane"

    def __str__(self):
        """Method's called when we convert the object to string"""
        return "{0} {1}".format(self.first_name, self.last_name)


class SpecialAgent(Person):
    """class describes a special agent, and it herites from Person class"""

    def __init__(self, last_name, registration_number):
        """Constructor, Agent's defined by its last name and registration number"""
        Person.__init__(self, last_name)
        self.registration_number = registration_number

    def __str__(self):
        """Method called durring a conversion to the string"""
        return "Agent {0}, Registration Number {1}".format(self.last_name, self.registration_number)


agent = SpecialAgent("Fisher", "18545-842")
print(agent.first_name)

print(issubclass(Person, SpecialAgent))
print(isinstance(agent, Person))