# Auteur : William Turbide Auclair
# Date : 26 juin 2025
# Description :  Générer un mot de passe aléatoire selon des critères (longueur, majuscules, chiffres, symboles).
#                modules standard (random, string), fonctions.
#                Interface utilisateur avec Tkinter ou CLI.
import random
import string

def generate_password(size, special_chars, digits, uppercase):
    if size <= 0 or size > 30 :
        raise ValueError("size must be between 1 and 30")

    if digits and uppercase and not special_chars:
        return ''.join(random.choices(string.digits + string.ascii_letters, k=size))
    elif digits and not uppercase and not special_chars:
        return ''.join(random.choices(string.digits + string.ascii_lowercase, k=size))
    elif not digits and not uppercase and not special_chars:
        return ''.join(random.choices(string.ascii_lowercase, k=size))
    elif digits and uppercase and special_chars:
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size))
    elif digits and not uppercase and special_chars:
        return ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=size))
    elif not digits and uppercase and special_chars:
        return ''.join(random.choices(string.ascii_letters + string.punctuation, k=size))
    elif not digits and not uppercase and special_chars:
        return ''.join(random.choices(string.ascii_lowercase + string.punctuation, k=size))
    elif not digits and uppercase and not special_chars:
        return ''.join(random.choices(string.ascii_letters, k=size))

    print(size, special_chars, digits, uppercase)
    return None

if __name__ == '__main__':
    try:
        longeur = int(input("Longeur (int): "))
        special = bool(input("Special chars (True ou False): "))
        print(special)
        nombre = bool(input("Digits (True or False): "))
        print(nombre)
        majuscule = bool(input("Uppercase (True or False): "))
        print(majuscule)

        print(generate_password(size=longeur, special_chars=special, digits=nombre, uppercase=majuscule))
    except ValueError:
        print("Valeur invalide.")