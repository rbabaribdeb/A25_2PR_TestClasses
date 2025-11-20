# Les exception : erreurs lors de l'execution du code
class WillException(Exception):
    pass

try:
    x = input ("svp entrer un nombre : ")
    print (10 / x)
except ZeroDivisionError: # capture l'exception spécifique ZeroDivisionError
    print("division par zero :: ")

except ValueError: # capture l'exception spécifique ValueError
    print("value error exception ")

except TypeError: # capture l'exception spécifique TypeError
    print("value error exception ")

except WillException : # capture l'exception spécifique TypeError
    print("value error exception ")

except Exception as e: # capture l'exception generale
    print("Autre exception :: ", e )

else: # exécuté dans le cas ou y a pas eu d'exception
    print("Tout s'st bien passé :) ")
finally:
    print("si ya eu ou pas eu d'erreur") # peut servir pour close un fichier



