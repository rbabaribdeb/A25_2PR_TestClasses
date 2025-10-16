# Constructeur
# Objectif : Encapsuler de la data
# Objectif : Ajouter du control au data = avoir de la cohérence

class Voiture:
    def __init__(self, a, p_modele, p_annee, p_km:int): # constructeur : methode qui retourne un objet
        self.marque = a
        self.modele = p_modele
        self.annee = p_annee # attribut publique
        self.__km = p_km # attribut protected
    def __str__(self):
        return "[Voiture : " + self.marque + "]"
    def get_km(self):
        return self.__km
    def set_km(self, km:int):
        if(km<0):
            print("Erreur : km negatif")
        elif (km<self.__km):
            print("Erreur : km inferieur au km enregistré")
        else:
            self.__km = km

# instantiation/création  de l'objet dans la mémoire
v1 = Voiture("toyota", "yaris", 2020, 50000)
v1.set_km(25000)
v1.set_km(-12555)
v1.set_km(75000)


print(v1.__str__()) ## equivalent print(v1)
print(type(v1))