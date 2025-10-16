# ville nom, pays, nombreHabitant
# capitale ville(nom, pays, nombreHabitant, monument)
# Heritage

class Ville:
    def __init__(self, nom, pays, nombreHabitant) :
        self.nom = nom
        self.pays = pays
        self.nombreHabitants = nombreHabitant

    def afficher(self):
        print("Ville : " + self.nom)


#################################################################

class Capitale(Ville):
    def __init__(self, ville, monument):
        super().__init__(ville.nom,ville.pays,ville.nombreHabitants)
        self.monument = monument
    def afficher(self):
        print("Capitale : " + self.nom + " monument " + self.monument )


