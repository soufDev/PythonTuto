class Counter:
    """this class has a class attribute that
        increments each time you create an object
        of this type"""
    counter = 0

    def __init__(self):
        """each time you create an object,
            you increment the counter"""
        Counter.counter += 1

    def how_many(cls):
        """Class Method that displays how many
            objects have been created"""
        print("until now, {} objects were created".format(cls.counter))

    how_many = classmethod(how_many)


Counter.how_many()

a = Counter()
Counter.how_many()

b = Counter()
Counter.how_many()

print(b.__dict__)