# Auteur : William Turbide Auclair
# Date : 29 mai 2025
# Description : fonction qui prend un int. S'il est divisible par 3 retroune fizz, par 5 retroune buzz
#                   et si divisible par 3 et 5 retourne fizz_buzz. sinon retroune le int entré

def fizz_buzz(nombre):
    if nombre % 3 == 0 and nombre % 5 == 0 :
        return "FizzBuzz"
    if nombre % 3 == 0 :
        return "Fizz"
    if nombre % 5 == 0 :
        return "Buzz"
    return nombre


while True :
    try :
        nombre = int(input("Enter nombre (-1 pour quitter) : "))
    except ValueError :
        print("Erreur : entrer un nombre entier.")
    else :
        if nombre == -1:
            break
        print(fizz_buzz(nombre))

