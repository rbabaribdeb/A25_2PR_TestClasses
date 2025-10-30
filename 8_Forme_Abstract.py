# Exemple de classe abstraite
# Mettre en evidence Le polymorphisme / heritage / abstraction

# Une classe abstraite possède une méthode abstraite ou plusieurs
# Cette méthode doit etre redefinie par les classes enfants (concretes)
# Avoir du polymorphisme

from abc import ABC, abstractmethod
from math import pi


class Forme(ABC): # class Forme [Abstraite]
    @abstractmethod # methode qui n'a pas de code
    def aire(self):
        pass

class Rectangle(Forme):  # classe rectangle herite de forme [Concrete]
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur
    def aire(self):
        return self.largeur * self.largeur


class Cercle(Forme): #[Concrete]
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return pi * self.rayon * self.rayon


# Methode calculePerimetre calculSurface

r1 = Rectangle(10,10)  # instancier la classe Rectange : créer un objet
c1 = Cercle(10)


# concequence de l'héritage
list = [] # c'est une liste de formes
list.append(r1)
list.append(c1)


# illustration du polymorphisme [liste] contient des formes:
# peut imorte le type dans liste on traite les objets
somme = 0
for f in list:
    somme = somme +  f.aire()
print("somme : " + str(somme))

f1 = Forme() # Empecher l'instanciation de cette classe

print(type(list[1]))