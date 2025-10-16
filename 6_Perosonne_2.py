# Utilisation des classes : créer des objets
# Polymorphisme



from Personne import Personne
from Personne import Etudiant,Enseignant

p1 = Personne("Bourbonniere","will","will.b@gmail")
p2 = Personne("Babari", "Raouf", "raouf@gmail.com")


en1 = Enseignant(p2,"4564","INFO")

et1 = Etudiant(Personne("LeBlanc","Jean Marie","jm.leblanc@gmail.com"),
               "789654",
               "INFO")

et2 = Etudiant(p1,"45654","INFO")
print(en1)
print(et1)
print(et2)

# Poly morphisme : plusieurs formes :
# comportement similaire pour des objets de type different
# a condition que ces objets partage un parent commun


# moi en tant que personne et un ecran sommes des ObjetPhysiques
# attributs communs : coordonnées, poids,
# comportement commun : deplacer, rotate,

# Methode polymorphe : a le meme nom chez le parent et l'enfant
# mais :: le code est different d'une methode à l'autre

liste = [p1, p2, en1, et1, et2]


# comportement similaire
for x in liste:
    print(x.redigerMail())
