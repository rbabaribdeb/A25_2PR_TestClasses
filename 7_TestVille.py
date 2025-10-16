# POO : 1 Encapsulation, 2 Héritage, 3 Polymorphisme, 4 Abstraction (Qu'on a pas vu encore ...)


from Ville import Ville, Capitale

v1 = Ville("montreal", "quebec",400000)

c1 = Capitale(Ville("Ottawa", "Canada", 200000), "Parlement" )

l = [v1,c1]

for x in l:
    x.afficher()