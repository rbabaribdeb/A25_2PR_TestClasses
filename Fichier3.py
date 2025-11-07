# Fichier 3 Ouvrir en liecture
import os


chemin   = "C:/Users/rbaba/PycharmProjects/TestClasses/dossier/"
fichier  = "data.txt"

# print(chemin + fichier) tester que le cheimn est correcte

f = open(chemin+fichier, 'r')
contenu = f.read()
print(contenu)
f.close()

