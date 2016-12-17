class BlackBord:
    """class defining a surface where we can write something"""

    def __init__(self):
        """Our Surface is empty by default"""
        self.surface = ""

    def surface_writing(self, message):
        """a method for writing on the table surface"""
        if self.surface != "":
            self.surface += "\n"
            self.surface += message
            return

        self.surface += message

    def surface_reading(self):
        """a method for reading what we write on the table"""
        print(self.surface)

    def surface_clear(self):
        """a method for clear what we write on the table"""
        self.surface = ""


blackBord = BlackBord()

blackBord.surface_reading()

blackBord.surface_writing("Hello World")
blackBord.surface_reading()

blackBord.surface_writing("Merry Christmas")
blackBord.surface_reading()


