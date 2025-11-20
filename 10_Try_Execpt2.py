# Les exception : erreurs lors de l'execution du code

try:
    x = input ("svp entrer un nombre : ")
    print (10 / x)
except ZeroDivisionError: # capture l'exception spécifique
    print("division par zero :: ")

except ValueError: # capture l'exception spécifique
    print("value error exception ")

except Exception as e: # capture l'exception generale
    print("Autre exception :: ", e )


