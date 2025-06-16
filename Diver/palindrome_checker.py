# Auteur : William Turbide Auclair
# Date : 13 juin 2025
# Description : Vérifier si une chaîne entrée par l’utilisateur est un palindrome.
#               Ignorer les espaces et la ponctuation.
from mercurial.utils.cborutil import BREAK

# En O(n2)
def palindrome_checker(mot):
    mot = mot.lower().replace(" ", "")
    while mot != "" :
        if not mot[0].isalpha():
            mot = mot[1:]
        elif not mot[-1].isalpha():
            mot = mot[:-1]
        elif mot[0] != mot[-1] :
            return False
        mot = mot[1:-1]
        print(mot)

    return True


# Version plus efficace trouver sur internet. en O(n)
#def palindrome_checker(mot):
#    lettres = [c.lower() for c in mot if c.isalpha()]
#    return lettres == lettres[::-1]



while True :
    chaine = input("Entré un mot a vérifier (QUIT pour quitter le program) : ")
    if chaine == "QUIT" :
        break
    print(palindrome_checker(chaine))