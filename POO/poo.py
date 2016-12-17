class Voiture:

    roues = 4
    moteur = 1

    def __init__(self):
        self.nom = "Soufiane"

    def allumer(self):
        print("La Voiture demarre")

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value


class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"

    def allumer(self):
        print("La voitre {0} demarre".format(self.nom))


voiture = Voiture()
voitureSport = VoitureSport()
voitureSport.nom = "A5"
voitureSport.allumer()
print(voiture.nom)
print(voitureSport.nom)