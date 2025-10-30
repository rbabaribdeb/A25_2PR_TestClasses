# variable de classe( comune ) vs variable instance (specifique a chaque objet )

# Methodes d'instance : agissent sur l'instance
# Methodes de classe : agissent sur la classe elle meme
# Methodes statique  : n'agit ni sur la classe ni sur l'instance

class Outils:
    compteur1 = 0
    def __init__(self, c):
        Outils.compteur1 += 1 # incrementer le compteur var de classe variable de classe
        self.compteur2 = c    # variable de instance

    # methode d'instance : agissent sur l'objet (instance self)
    def methode(self):
        print(self.compteur2)

    @classmethod
    def getcompte(cls): # cls classe : agissent sur la classe
        return cls.compteur1


    @staticmethod # agit ni sur la classe ni sur l'objet
    def addition(a, b ):
        print("methode independante... total " + str(a+b))



o1 = Outils(5)
o2 = Outils(4)
o3 = Outils(7)
o4 = Outils(7)

# modifie puor tous les objets de la classe [var classe]
# modifie puor seulement  l"objets o3 de la classe [var instance]

print(o3.getcompte())

o3.getcompte()
Outils.getcompte() # [methode de classe]


str.islower("hi") # methode reliée à la classe ()
"hi".islower() # methode reliée à l'objet (self)


Outils.addition(3,5)
o3.addition(3,5)

