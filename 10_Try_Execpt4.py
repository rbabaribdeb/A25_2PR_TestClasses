# Les exception : erreurs lors de l'execution du code
class AgeException(Exception): # mauvaise pratique
    pass

def input_age():
    age = int(input("Enrer votre age")) #-25
    if age < 0:
        raise AgeException("L'age ne peut etre negatif") # provoquer une exception volontaire ...
    return age

try:
    age = input_age()
except Exception as e:
    print("exception .... ", e)
