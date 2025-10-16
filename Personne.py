# Heritage : fabrique une nouvelle classe a partir de classe existante
# classe parent vs classe enfant
# classe enfant = classe parent + nouveaux attributs et/ou nouvelles méthodes

# exemple  : DATA / FAIRE
# Personne : nom, prenom, email / setNom() / envoyerUnMail()
# Etudiant : Personne + numDA + Programme / sinscrireProgramme()
# Enseignant : Personne + numEmploye + Departement / setDepartement()

# Un Etudiasnt "est une" Personne = lien d'heritage
#######################################################################################
class Personne:
    def __init__(self, nom, prenom, mail): # Constructeur du parent
        self.nom = nom
        self.prenom = prenom
        self.mail = mail

    def __str__(self):
        return " Prsonne : " + self.nom + " " + self.prenom + " "

    def redigerMail(self):
        return "Mr Personne " + self.prenom + ".... corps du mail  "

#######################################################################################
class Etudiant(Personne):
    def __init__(self, personne, numDA, programme ): # Constructeur de l'enfant
        super().__init__(personne.nom, personne.prenom, personne.mail) # Appel au constructeur du parent
        self.numDa = numDA
        self.programme = programme

    def __str__(self):
        return " Etudiant : " + self.nom + " " + self.prenom + " " + self.numDa

    def redigerMail(self):
        return "Mr Etudiant " + self.prenom + "....." + self.numDa + " .... suite du mail"

########################################################################################
class Enseignant(Personne): # ()=herite de Personne
    def __init__(self,personne, numEmploye, dep):
        super().__init__(personne.nom,personne.prenom,personne.mail)
        self.numEmploye = numEmploye
        self.dep = dep

    def __str__(self):
        return " Enseignant : " + self.nom + " " + self.prenom  + " " + self.numEmploye

    def redigerMail(self): # Méthode polymorphe
        return "Mr Enseignant  " + self.prenom + "..... du departement ... " + self.dep