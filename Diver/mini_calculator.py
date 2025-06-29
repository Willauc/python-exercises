# Auteur : William Turbide Auclair
# Date : 13 juin 2025
# Description : Implémenter un mini-calculateur en ligne de commande supportant les opérations +, -, *, /.
#               Ajouter gestion des erreurs (ex: division par 0).

def calcule(equation):
    operante_gauche = ""
    operante_droite = ""
    operateur = ""
    operateur_passer = False
    equation = equation.replace(" ", "")

    for car in equation:
        if car.isalpha():
            raise ValueError
        if not operateur_passer and car.isdigit():
            operante_gauche += car
        elif not operateur_passer and not car.isdigit():
            operateur = car
            operateur_passer = True
        else:
            operante_droite += car

    if not operante_gauche or not operante_droite or not operateur:
        raise ValueError("Format invalide.")

    gauche = int(operante_gauche)
    droite = int(operante_droite)

    if operateur == "+":
        return gauche + droite
    elif operateur == "-":
        return gauche - droite
    elif operateur == "*":
        return gauche * droite
    elif operateur == "/":
        return gauche / droite
    elif operateur == "%":
        return gauche % droite
    else:
        raise ValueError("Operateur invalide.")


if __name__ == "__main__":
    while True:
        try:
            eq = input("Enter equation (ex : 2+2, QUIT pour quitter le program): ")
            if eq == "QUIT":
                break
            print("Résultat : ", calcule(eq))
        except ValueError:
            print("Invalid equation, lettre ou operateur non suporter.")
        except ZeroDivisionError:
            print("Invalid equation, division par zero impossible.")
