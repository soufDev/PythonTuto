class ZDict:
    """Classe enveloppe d'un dictionnaire"""

    def __init__(self):
        """Our Class doesn't accepts any parameter"""
        self._dictionary = {}

    def __getitem__(self, item):
        """this special method is called when you put object[item]
         it redirects to self._dictionary[item]"""
        return self._dictionary[item]

    def __setitem__(self, key, value):
        """this special method is called when you write object[key] = value
        On redirige vers self._dictionary[key] = value"""
        self._dictionary[key] = value

my_class = ZDict()
my_class["soufiane"] = "AIT AKKACHE"

print(my_class["soufiane"])