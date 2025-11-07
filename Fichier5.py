# Fichier 5 Ouvrir en lecture ligne pa ligne
import os

chemin   = "C:/Users/rbaba/PycharmProjects/TestClasses/dossier/"
fichier  = "data.txt"

# print(chemin + fichier) tester que le cheimn est correcte
f = open(chemin+fichier, 'r')
tabLigne = f.readlines()
a = tabLigne[1].split(',')
print(a[1])

f.close()


