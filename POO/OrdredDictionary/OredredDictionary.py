# -*-coding:Latin-1 -*
class OrdredDictionary:
    """class to define an oredred dictionary it heritates from dict class"""

    def __init__(self):
        self._keys = []
        self._values = []

    def __setitem__(self, key, value):
        self._keys.append(key)
        self._values.append(value)

    def __str__(self):
        temp = ""
        if len(self._keys) == 0:
            return "{}"
        else:
            for i in range(len(self._keys)):
                if i == len(self._keys)-1:
                    temp += "'{0}': '{1}'".format(self._keys[i], self._values[i])
                else:
                    temp += "'{0}': '{1}'".format(self._keys[i], self._values[i]) + ", "

        return "{ "+temp+" }"

    def __delitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            del self._keys[index]
            del self._values[index]
        else:
            raise AttributeError

    def __len__(self):
        return len(self._keys)

    def __add__(self, other):
        for key in other.keys:
            self._keys.append(key)

        for value in other.values:
            self._values.append(value)

        return self

    def reverse(self):
        self._keys = list(reversed(self._keys))
        self._values = list(reversed(self._values))
        return self

    def items(self):
        for i in range(len(self._keys)):
            yield self._keys[i], self._values[i]

    def __contains__(self, item):
        return item in self._keys

    def _get_keys(self):
        return self._keys

    def _get_values(self):
        return self._values

    keys = property(_get_keys)
    values = property(_get_values)

order = OrdredDictionary()
order1 = OrdredDictionary()
order["soufiane"] = "AIT AKKACHE1"
order["Lakhdar"] = "AIT AKKACHE2"
order["samir"] = "AIT AKKACHE3"
order["Mourad"] = "AIT AKKACHE4"

order1["Slimane"] = "ALI AHMED1"
order1["Toufik"] = "ALI AHMED2"
order1["Ghani"] = "ALI AHMED3"

del order['soufiane']
print(order)
order += order1

print(len(order))
print(order)
print(order.reverse())
print(order.keys)
print(order.values)

for k, v in order.items():
    print(k, ', ', v, '\n')


