# Fichier 2
import os

# lien relatif : dossier data
# . dossier actuel
## .. dossier parent
# lien absolut
chemin   = "C:/Users/rbaba/PycharmProjects/TestClasses/dossier/"
fichier  = "fichier.txt"

# utiisation de lien relatif
#os.mkdir("./dossier")

# utiisation de lien absolut
#  print(chemin + fichier) # test
#os.mkdir(chemin)
cheminfichier = chemin + fichier
print(cheminfichier)
f = open(chemin + fichier,'w')

f.write("M,Roaouf,1999")


