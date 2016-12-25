# -*-coding:Latin-1 -*

from _operator import attrgetter


class Students:
    """Class that Describe Students"""

    def __init__(self, name, age, avg):
        """Constructor For the student and initialize all arguments"""
        self.name = name
        self.age = age
        self.avg = avg

    def __repr__(self):
        """print information about students"""
        return "<Student {} (age={}, avg={}>".format(self.name, self.age, self.avg)


students = [
    Students("Clément", 14, 16),
    Students("Charles", 12, 15),
    Students("Oriane", 14, 18),
    Students("Thomas", 11, 12),
    Students("Damien", 12, 15),
]

print(sorted(students, key=attrgetter("age", "avg", "name"), reverse=True))