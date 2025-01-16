"""
history = ["apple"]
print(history)
history.clear()
print(history)
"""
"""
hello = input("une chaine de caractere : ")

file = open('test.txt', 'a')
file.write(hello)
file.close()

file = open('test.txt', 'r')
for i in file:
    print(i.strip())
file.close

"""

import csv
def main():
    donnees = []
    while True:
        while True: 
            try:
                number1= int(input("entrez un chiffre : "))
                break
            except ValueError:
                print("veuillez entrez un nombre")


        
        donnees.append(number1)

        with open('test.csv', 'w', newline='') as fichier:
            writter = csv.writer(fichier)
            writter.writerow(donnees)

        with open('test.csv', 'r') as file:
            read = csv.reader(file)
            for i in read:
                print(i)


        print(donnees)

        choix = input("voulez vous supprimer un element Y/N : ").upper()

        if choix == "Y":
            choix2 = int(input(f"veuillez indiquez le chiffre que vous voulez suppprimer entre 0 et {len(donnees)-1}"))
            del donnees[choix2 ]
            with open('test.csv', 'w', newline='') as fichier:
                writter = csv.writer(fichier)
                writter.writerow(donnees)
            print(donnees)
        else:
            print(donnees)
main()
