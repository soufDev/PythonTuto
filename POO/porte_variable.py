# -*-coding:Latin-1 -*

a = 8


# fonction qui affiche la valeur de la variable a
def print_a():
    print("la varibale a = {0}".format(a))

print_a()


def set_var(ma_variable):
    try:
        print("Avant l'affectation notre variable var vaut {0}".format(var))
    except NameError:
        print("La variable var n'existe pas encose")
    var = ma_variable
    print("Apres l'affectation, notre variable var vaut {0}".format(var))


set_var(6)

