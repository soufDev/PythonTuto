# -*-coding:Latin-1 -*
import pickle


# a chaque foie qu'on joue un coups en decrement le nbre de coups restant
def remaining_shots(shots_nb):
    shots_nb -= 1
    return shots_nb


# si le fichier exsits alors renvoyer le contenu sinon renvoyer -1
def file_exist(file_name):
    try:
        with open(file_name, 'r') as my_file:
            return pickle.Unpickler(my_file).load()
    except FileNotFoundError:
        return -1


# cr�e le fichiers s'il n'est pas encore cr�e ou bien renvoyer le contenu du fichier
def create_file_if_not_exist(file_name):
    with open(file_name, 'wb') as my_file:
        return pickle.Pickler(my_file)


# recuperer les scores dans un dictionnaire et s'il est vide on revoie -1
def get_scores(file_name):
    scores = file_exist(file_name).copy()
    if scores != -1:
        return scores
    else:
        create_file_if_not_exist(file_name)
        return {}


# voir si le joueur exist dej�
def player_exist(scores, playerName):
    if playerName in scores.keys():
        return True
    else:
        return False


# enregister les scores
def save_scores(file_name, scores):
    with open(file_name, 'wb') as my_file:
        pickle.Pickler(my_file).dump(scores)


# Fonction pour enregister les nom des joueurs qui n'existe pas dans le fichier
def sign_name(player_name, scores, file_name):
    if not player_exist(scores, player_name):
        scores[player_name] = 0
        save_scores(file_name, scores)


# fonctions pour mettre a jour les score
def update_score(player_name, scores, file_name, new_score):
    scores[player_name] = new_score
    save_scores(file_name, scores)


# fonction chercher une lettre dans un mot
def search(word, letter):
    if letter in list(word):
        word_liste = list(word)
        for i in range(len(word_liste)):
            if letter != word_liste[i]:
                word_liste[i] = "*"
        word = "".join(word_liste)

    return word


# compter combien d'etoile y'en a dans le mot en final
def stars_count(word):
    word_list = list(word)
    stars = 8
    for i in range(len(word_list)):
        if word_list[i] == "*":
            stars -= 1
    return stars


# fonction qui ne retourn le score selon le mot en final
def find_score(word):
    if word.find("*") == -1:
        return 8
    else:
        return stars_count(word)

def find_score():
    return soufiane
