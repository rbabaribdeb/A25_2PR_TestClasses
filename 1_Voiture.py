# Objectif : Regrouper de la data


# declaration de la classe
# Le nom de la classe commence avec une maj
# Les attributs sont marque, modele, annee commencent avec min
class Voiture:
    marque = ""
    modele = ""
    annee = ""
   # __km = 150000


# instantiation/création  de l'objet dans la mémoire
v1 = Voiture()
v1.marque = "volvo"
v1.modele = "C90"
v1.annee = 2019

v2 = Voiture()

print(v1)
print(type(v1))