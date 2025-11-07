# Fichier 6 Ouvrir en lecture ligne pa ligne
import csv
import os

chemin   = "C:/Users/rbaba/PycharmProjects/TestClasses/dossier/"
fichier  = "data.txt"

# print(chemin + fichier) tester que le cheimn est correcte
f = open(chemin+fichier, 'r')
matrice =[]
reader = csv.reader(f,delimiter=',')
for ligne in reader:
    matrice.append(ligne)

print(matrice[2][1])

