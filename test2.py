
nom= "emma"

def afficher(truc):
    print(f"hello {truc} ")

afficher(nom)

def nombre():
    num1 = int(input("rentrez une valeur"))

    resultat = num1 + num1
    return resultat

res = nombre()

print(res)