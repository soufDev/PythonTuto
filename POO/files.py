import os

os.chdir("/home/soufiane/Documents")
"""
fichier = open("fichier.txt", "r")

liste = fichier.read().split("\n")
liste = [item for item in liste if item != '']
print(liste)

fichier.close()
"""

# alternative
with open("fichier.txt", "r") as fichier:
    liste = fichier.read().split("\n")
    liste = [item for item in liste if item != '']
    print(liste)

import pickle
# PICKLE library
score = {
    "joueur1": 45,
    "joueur2": 85,
    "joueur3": 55,
    "joueur4": 25
}

with open('donnees', 'wb') as fichier:
    mon_pickle = pickle.Pickler(fichier)
    mon_pickle.dump(score)
    score = {
        "joueur1": 45,
        "joueur2": 85,
        "joueur3": 55,
        "joueur4": 28
    }
    mon_pickle.dump(score)

with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    #result = mon_depickler.load()
    print(mon_depickler.load())
    print(mon_depickler.load())
