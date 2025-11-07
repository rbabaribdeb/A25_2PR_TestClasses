# Fichier 4 Ouvrir en lecture ligne pa ligne
import os


chemin   = "C:/Users/rbaba/PycharmProjects/TestClasses/dossier/"
fichier  = "data.txt"

# print(chemin + fichier) tester que le cheimn est correcte

f = open(chemin+fichier, 'r')
tabLigne = []

while True:
    ligne = f.readline()
    print(ligne)
    if ligne == "":
        break
    tabLigne.append(ligne)

f.close()


