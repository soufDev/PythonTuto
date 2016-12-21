# -*-coding:Latin-1 -*
class RevStr(str):

    def __iter__(self):
        return ItRevStr(self)


class ItRevStr:

    def __init__(self, search):
        self.search = search
        self.position = len(search)

    def __next__(self):
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.search[self.position]

chaine = RevStr("Soufiane AIT AKKACHE")

for c in chaine:
    print(c)


def intervalle(borne_inf, borne_sup):
    """Generateur Parcourant la serie des entiers entre la borne_inf et brone_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None:  # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
        borne_inf += 1

generator = intervalle(5, 25)
for i in generator:
    if i == 15:
        generator.send(18)
    print(i,end=" ")
