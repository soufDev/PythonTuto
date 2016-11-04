# -*-coding:Latin-1 -*

chaine = "      bonjour tout le monde !     "
chaine1 = "soufiane"
chaine2 = "AIT AKKACHE"
print("hello {0} mon nom c'est {1}".format(chaine1, chaine2))
print("chaine = ", chaine.lower())
print("chaine = ", chaine.upper())
print("chaine = ", chaine.strip().capitalize())
print("chaine = ", len(chaine.strip()))
print("chaine = ", len(chaine.upper().strip().center(50)) )

liste = [
    ("fraises", 76),
    ("prunes", 51),
    ("pommes", 22),
    ("poires", 18),
    ("melons", 4),
]

liste1 = [(q, n) for (n, q) in liste]
liste = [(n, q) for (q, n) in sorted(liste1, reverse=True)]

def function_inconnue(*parametre_non_nommes, **parametres_nommes):
    """fontion permettant de voir comment recuperer les parametres nommés
     dans un dictionnaire"""
    print("j'ai reçu en parametres nom nommés: {}".format(parametre_non_nommes))
    print("j'ai reçu en parametres nommés: {}".format(parametres_nommes))

function_inconnue("ait akkache", 5, 8, p=4, a=5, c="soufiane") #avec aucun parametres

parametres = {'sep': ' >> ', 'end': '-\n'}
print("Voici", "un", "example", "d'appel", **parametres)