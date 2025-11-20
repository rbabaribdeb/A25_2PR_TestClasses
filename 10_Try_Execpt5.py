# Les exception : erreurs lors de l'execution du code

try:
    f = open("data.txt", "r")
    contenu = f.read()
except FileNotFoundError:
    print("Fichier n existe pas")
except Exception as e:
    print("autre exception levee")

finally:
    try:
        f.close()
    except:
        pass # on ignore si on a pas ete capable d'ouvrir le d=fichier

