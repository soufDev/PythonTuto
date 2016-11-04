# -*-coding:Latin-1 -*
"""TP casino pour la roue"""
import random



def meme_couleur(num_choisis, num_roue):
    """voir si le numero choisis et de la meme
    couleur que celui retourné par la roue"""
    if(num_choisis % 2 == 0) and (num_roue % 2 == 0):
        return True
    elif (num_choisis % 2 == 1) and (num_roue % 2 == 1):
        return True
    return False


def tourner_la_roue():
    """tourner la roue et voie le numéro retourné"""
    numero_roue = random.randrange(50)
    print("Le numero de la roue est : ", numero_roue)
    return numero_roue


def gain(num_choisis, mise):
    """retourné les gains"""
    numero = tourner_la_roue()
    if num_choisis == numero:
        return mise * 3
    elif meme_couleur(num_choisis, numero):
        return mise / 2
    else:
        return 0


def num_choisi():
    nb_choisis = int(0)
    try:
        nb_choisis = input("Choisir votre numero : ")
        nb_choisis = int(nb_choisis)
        assert (nb_choisis < 50) and (nb_choisis >= 0)
        return nb_choisis
    except TypeError:
        print('Probleme de Valeur !')
        return -1
    except AssertionError:
        print('Vous vous etes tremper dans la case choisie !')
        return -1
    except ValueError:
        print('Probleme de Valeur !')
        return -1


def mise():
    argent = 0
    try:
        argent = input('veuillez entrer votre mise : ')
        argent = int(argent)
        assert argent > 0
        return argent
    except AssertionError:
        print('Vous devez entrez une mise positive !')
        return -1
    except TypeError:
        print('Veuillez entrer un numero !')
        return -1
    except ValueError:
        print('Probleme de Valeur !')
        return -1


def casino():
    quitter = ''
    nb_choisi = int(0)
    argent = int(0)
    while quitter != 'q':
        nb_choisi = num_choisi()
        if nb_choisi == -1:
            continue
        argent = mise()
        if argent == -1:
            continue
        combien_de_gain = gain(nb_choisi, argent)
        if combien_de_gain == 0:
            print('vous avez perdu votre mise')
        else:
            print('votre gain est de : ', combien_de_gain)
        quitter = input('tapez une q pour quitter ou autre pour rejouer')


casino()