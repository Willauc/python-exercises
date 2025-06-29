# Auteur : William Turbide Auclair
# Date : 06 juin 2025
# Description : fonction qui retroune le caractére le plus fréquent dans un string.

phrase = "this is a common interview question"

frequence = {}
for car in phrase:
    if car in frequence:
        frequence[car] += 1
    else:
        frequence[car] = 1

# En O(n)
plusFrequent = ""
for car in frequence:
    if plusFrequent == "":
        plusFrequent = car
    else:
        if frequence[car] > frequence[plusFrequent]:
            plusFrequent = car

# Alternative en O(n log n) :
# frequence_trier = sorted(frequence.items(), key=lambda x: x[1], reverse=True)
# print(frequence_trier[0])

print(plusFrequent, " est le caractere le plus frequent!")
