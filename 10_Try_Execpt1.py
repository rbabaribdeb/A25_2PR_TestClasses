# Les exception : erreurs lors de l'execution du code

try:
    x = input ("svp entrer un nombre : ")
    print (10 / x)
except ZeroDivisionError: # capture l'exception spécifique
    print("division par zero :: ")

except ValueError:
    print("value error exception ")

except Exception:
    print("Autre exception")


