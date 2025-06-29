# Auteur : William Turbide Auclair
# Date : 13 juin 2025
# Description :  Lire un fichier CSV avec les noms et notes d’étudiants
#                et afficher des statistiques : moyenne, meilleure note, etc.
#                Générer un rapport dans un fichier .txt.

import csv
import datetime
import os

nbr_etudiant = 0
cumulatif_note = 0
meilleur_note = 0
pire_note = 100
moyenne = 0

if not os.path.exists('etudian_stats.csv'):
    print("Fichier inexistant.")
else:
    with open('etudian_stats.csv', 'r') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ranger in lecteur:
            try:
                ranger['Note'] = int(ranger['Note'])
                nbr_etudiant += 1
                cumulatif_note += ranger['Note']
                if ranger['Note'] > meilleur_note:
                    meilleur_note = ranger['Note']
                elif ranger['Note'] < pire_note:
                    pire_note = ranger['Note']
            except (ValueError, KeyError):
                continue
    if (nbr_etudiant > 0):
        moyenne = cumulatif_note / nbr_etudiant

    statistique = f'''{datetime.datetime.now().strftime("%d/%m/%Y")}:\n
Nombre d'etudiant: {nbr_etudiant}
Meilleur note: {meilleur_note}
Pire note: {pire_note}
Moyenne: {moyenne}\n\n'''

    with open('statistique.txt', 'a') as stat_file:
        stat_file.write(statistique)
        os.startfile('statistique.txt')
