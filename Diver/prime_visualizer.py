# Auteur : William Turbide Auclair
# Date : 27 juin 2025
# Description : Générer tous les nombres premiers jusqu’à n et les afficher dans une grille (ex: 10x10).
#               Affichage graphique avec matplotlib ou pygame.

def est_premier(nombre):
    if nombre < 2:
        return False

    for n in range(2, int((nombre / 2) + 1)):
        if nombre % n == 0:
            return False
    return True


def nombres_premier(limite):
    progres = 2
    lst_nbr_premier = []
    while progres < limite:
        if est_premier(progres):
            lst_nbr_premier.append(progres)
            progres += 1
        else:
            progres += 1
    return lst_nbr_premier


def afficher_nombre_premier_console(lst_premier, limite_colone):
    present_colone = 1
    longeur = len(lst_premier)
    while longeur > 0:
        if present_colone < limite_colone:
            print("|", lst_premier.pop(0), end='')
            longeur -= 1
            if longeur == 0:
                print("|")
            present_colone += 1
        else:
            print("|", lst_premier.pop(0), end='|\n')
            present_colone = 1
            print("----" * limite_colone)
            longeur -= 1


afficher_nombre_premier_console(nombres_premier(1000), 10)

# def afficher_nombre_premier_graphique
