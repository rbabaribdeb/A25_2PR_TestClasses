# Fichier 1

# CSV : comma separated values
# CSV : compatible avec excel

# Ouverture d'un fichier en mode ecriture et a ajouter des lignes
# w write(ecrase)
# a append(ajouter à la fin de ce qui existe)

f = open("dossier/data.txt", 'a')
f.write("M, William, 1999 \n" )
f.close()
