# ce modules est consacré au fonctions pour la conversion de type
# les type : binaire et entier
import os

binaire = []

decimal = []
list_address = []
chose = ""


ip_ad = []

list_bits = []



"""nous mettons en place notre fonction menu pour diriger les utilisateurs--------------
---------- cette fonction permettra de effectuer une presentation de choix que peux faire un utilisateur avec ce code:
1. pour la conversion d-une adresse ip decimale en bianire 
2. pour la conversion d'une adresse ip établie en binaire en decimale
3. demande à l'utilisateur s'il veut continuer à effectuer des conversions.


"""


def menu():

    print()
    print()
    print("---------------------Ip Cconverter-----------------------".upper().center(100))

    print()
    print()
    print()
    print("Effectuez un choix d'Opération:".center(90))

    print()

    print("1.Pour effecuter une conversion binaire de votre adresse IPV4.".center(74))

    print()

    print("2.Pour effectuer une conversion decimale de votre adresse IPV4.".center(75))

    print()

    print("3.Pour inclure un fichie contenant les valeurs à convertir.".center(72))
    print()

    print("0.Entrez 0 pour quitter le programme.".center(50))

    print()



"""nous créons une fonction appelé conv_binaire, pour effectuer la conversion en bit d'une adresse ip décimale qu'elle reçoit"""


def conv_binaire(args): # cette fonction à pour de convertir les adresse ip decimales en bits

    args = str(args) # ici , on met le type du parametre en chaine de caractère

    ipv = args.split(".") #par la suite on decompose notre chaine de caractère pour former une liste en prenant le "." comme delimiteur

    
    for x in ipv: #dans notre liste nommé ipv, nous reccuperons chaque élement de la liste pour le traitement

        try: #ici, nous effectuons un test de conversion de type pour excepter d'eventuelle erreurs

            x = int(x) #on effectue une conversion de l'élement x pris dans la liste ipv en entier

        except ValueError: # nous exceptons le valeur de conversion

            print("Erreur de conversion")

            break # en cas d'erreur de conversion le programme s'arret immediatement

        bit = bin(x) #ici une conversion en binaire de l'entier est effectuée

        bit = bit[2:] # cette partie, permet de recupper la partie essentielle apres la conversion excepté le "0b" 

        binaire.append(bit)# là, nous ajoutons notre binaire dans la liste binaire
    
    ipv4_bit = ".".join(binaire)#ici nous effectuons une jointure de nos differents élements de notre liste pour former une seule chaine

    return ipv4_bit# cette partie permet de retourner adresse ip convertir en binaire






"""Cette deuxième fonction o pour but de convertir toute valeur binaire en valeur decimale. Alors cette fonction permettra 
de determiner la valeur decimale d'une valeur binaire
"""


def conv_ent(args):

    args = str(args)#conversion en chaine de caractère

    bits = args.split(".") 

    for bit in bits:

        try:

            bit = int(bit,2)#permet de determiner la valeur décimale de du binaire entré

            bit = str(bit) #on passe la valeur décimale en type chaine de caractère pour permettre la jointure

        except ValueError:

            print("Erreur de type!!")

            break

        decimal.append(bit)

        ip = ".".join(decimal)


    return ip



#partie 2, elle consistera à faire deux fonction qui permettrons d'extaire des adresses ip d'un fichier pour les les calculer et 
#les réenregistrer dans un fichier à nouveau



def get_file(file, dir_name): #cette fonction permet de reccuperer les ligne d'élément dans un fichier et de les envoyer sous forme de liste


        repertoire = os.chdir(dir_name) # permet de definr le repertoir où sera enregistré le fichier

        with open(file, "r") as f:

            liste = f.readlines() #ramène les lignes sous forme de liste 

        return liste #ici la fonction retourne  une liste





# une fonction qui permettra de d'engistrer les resultats dans un fichier 


def register(file, dir_name, value):#cette fonction permet d'enregistrer les donnéé fournier par l'utilisateur ou le programme dans un fichier
        
        os.chdir(dir_name) #permt de changer de repertoire selon ce que l'utilisateur aurait fourni comme nom de repertoire


        with open(file, "a") as f:
             
             f.write(value + "\n") # permet d'engistre les donner un fichier par ligne et en y ajoutant des sauts de ligne
       



# nous allons créer une fonction pour l'option trois, dont celle de travailler sur une liste contenant soit des ip binaires ou decimale




def ip_filecalcule_bits(*ip_liste):

        for ip in ip_liste:

            ip = str(ip)

            ip = ip.strip()

            entier = ip.split(".")

            bits = ""
            binaire = []
            address = ""
            for ent in entier:

                ent = int(ent)

                bits = bin(ent)

                bits = str(bits)

                binaire.append(bits[2:])

            address = ".".join(binaire)


            list_bits.append(address)

        return list_bits







#calcul décimal des adresses ip binaiare à parti d'un fichier


def ip_filecalcule_dec(*liste_ip):

        for ip in liste_ip:

                ip = str(ip)

                ip = ip.strip()

                bit_liste = ip.split(".")

                decimal = []

                ip_ad = ""

                for bit in bit_liste:

                    entier = int(bit,2)

                    entier = str(entier)

                    decimal.append(entier)

                ip_ad = ".".join(decimal)

                list_address.append(ip_ad)
            
        return list_address



