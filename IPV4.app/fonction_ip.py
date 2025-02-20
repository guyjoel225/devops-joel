# ce modules est consacré au fonctions pour la conversion de type
# les type : binaire et entier

binaire = []

decimal = []

chose = ""




"""nous mettons en place notre fonction menu pour diriger les utilisateurs--------------
---------- cette fonction permettra de effectuer une presentation de choix que peux faire un utilisateur avec ce code:
1. pour la conversion d-une adresse ip decimale en bianire 
2. pour la conversion d'une adresse ip établie en binaire en decimale
3. demande à l'utilisateur s'il veut continuer à effectuer des conversions.


"""


def menu():

    print("---------------------Ip Cconverter-----------------------".upper().center(100))

    print()

    print("Effectuez un choix d'Opération:")

    print()

    print("1.Pour effecuter une conversion binaire de votre adresse IPV4!")

    print()

    print("2.Pour effectuer une conversion decimale de votre adresse IPV4!")

    print()

    print("0.Entrez 0 pour quitter le programme!")



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

