# -*-coding:latin-1 -*

stopValue = ''
###############################
def is_bissextile(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    else:
        return False
################################
while stopValue != 'f':
    try:
        print('\nTapez l\'ann�e que vous voulez ')
        enterValue = input()
        enterValue = int(enterValue)
    except ValueError:
        print('\nVeuilez Tapez une ann�e valide !')
        continue

    if is_bissextile(enterValue):
        print('\ncette ann�e est Bissextile')
    else:
        print('Desol� cette ann�e n\'est pas Bissextile :( ')

    print('\nSi vous voulez continuer entrer un valeur differentes de "f" ')
    stopValue = input()

print('MERCI D\'AVOIR JOUER AVEC NOUS')




