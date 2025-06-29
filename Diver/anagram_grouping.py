# Auteur : William Turbide Auclair
# Date : 25 juin 2025
# Description : Grouper une liste de mots par anagrammes.
#               Entrée : ["chien", "niche", "chein", "hello", "ohlle"]
#               Sortie : [['chien', 'niche', 'chein'], ['hello', 'ohlle']]
#               Ajouter une interface CLI ou utiliser argparse.
import sys


# lst_anagrammes = ["chien", "niche", "chein", "hello", "ohlle", "montreal", "MONTREAL   "]

def anagram_grouping(lst_anagrammes):
    lst_anagrammes_groupe = []
    for anagram in lst_anagrammes:
        anagram_mod = anagram.lower().replace(" ", "")
        anagram_trier = sorted(anagram_mod)
        mot_placer = False

        for lst_anagramme in lst_anagrammes_groupe:
            premier_mot = sorted(lst_anagramme[0].lower().replace(" ", ""))
            if premier_mot == anagram_trier:
                dejas_present = False
                for mot in lst_anagramme:
                    if mot.lower().replace(" ", "") == anagram_mod:
                        dejas_present = True
                        mot_placer = True

                if not dejas_present:
                    lst_anagramme.append(anagram)
                    mot_placer = True
                    break
        if not mot_placer:
            lst_anagrammes_groupe.append([anagram])
    return lst_anagrammes_groupe


if __name__ == "__main__":
    # print(anagram_grouping(lst_anagrammes))

    print(anagram_grouping(sys.argv[1:]))
