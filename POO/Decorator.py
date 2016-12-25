# -*-coding:Latin-1 -*
def mon_decorateur(fonction):
    """Notre decorateur: il va afficher un message
    avant l'appel de la fonction définie"""


    def fonction_modifiee():
        """Fonctions que l'on va renvoyer"""
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()

    return fonction_modifiee

@mon_decorateur
def salut():
    print("Salut !")

print(salut)