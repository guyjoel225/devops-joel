import os


path = "/home/joel/Bureau"

os.chdir(path)

def ecrire_file(message,file_name):

        fichier = open(file_name, "a")

        ecrire = fichier.writelines(message+"\n")

        fichier.close()



def lire_file(file_name):

            fichier = open(file_name, "r")

            lire = fichier.read()
            fichier.close()

            print(lire)

continuer = True

message = ""

nom_fichier = ""

print("c'est en écrivant un mot, que le gout d'en ecrire d'autre vient")
print()

print("double cliquez sur Enter pour ajouter une nouvelle ligne")
print()

print("pour quitter, appuyez sur Enter et entrez la lettre q pour quitter")
print()

nom_fichier = input("entrez le nom de votre fichier: ")

"""
while continuer:
        
        
        print()

        message = input()

        ecrire_file(message, nom_fichier)
        quiter = input().lower()

        if quiter == "q":
                
            continuer = False

        else:
                continuer = True


lire_file(nom_fichier)
"""

# usage de with pour eviter de tout le temps fermer le fichier, qu'on utilise
print()
print()

texte = input("Entez votre texte ici : ")
"""

with open(nom_fichier, "w") as f:
        
        ecrire = f.write(texte)

with open(nom_fichier,"r") as f:
        
        afficher = f.readline()

print()

print("On affiche le texte entré ici")
print()
print(afficher)

"""

def Ecrire(message, file_name):
        
        with open(file_name, "a") as f:
                
                f.writelines(message+"\n")


def Lire(file_name):
        
        with open(file_name, "r") as f:
                
                return f.read()
        



Ecrire(texte, nom_fichier)

print(Lire(nom_fichier))


with open(nom_fichier, "r") as f:

        position = f.seek(4,0,1)

        print(position)

