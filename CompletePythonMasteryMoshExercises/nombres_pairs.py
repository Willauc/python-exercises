# Auteur : William Turbide Auclair
# Date : 29 mai 2025
# Description : Affiche les nombres pairs entre 1 et 9
#               et indique combien de nombres pairs ont été trouvés.

nbr_retenue = 0
for nombre in range(1,10) :
    if nombre % 2 == 0 :
        print(nombre)
        nbr_retenue += 1
print(f"{nbr_retenue} nombre pair.")