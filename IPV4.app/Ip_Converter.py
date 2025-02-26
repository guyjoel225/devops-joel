from fonction_ip import *

continuer = True


while continuer:

    # appel de la fonction menu

    print()
    print()
    menu()

    print()
    print("\n")

    chose = input("Entrez un choix d'Opération svp!: ")

    try:

        chose = int(chose)
    
    except ValueError:

        continuer = True

        continue

    if chose == 1:

        print("\n")
        print()

        print("Vous avez opté pour une conversion binaire: ")

        print("\n")

        #appel de la fonction conv_binaire

        Add_decimale = str(input("Veuillez entrez votre adresse au format decimal ici: "))

        var = conv_binaire(Add_decimale)
        print()
        print("\n")

        print(f"La valeur binaire de votre adresse est: {var}")
        print("\n")
    
    elif chose == 2:

        print()
        print("\n")

        print("Vous avez opté pour une conversion decimale: ")

        print("\n")

        #appel de la fonction conv_ent

        add_binaire = str(input("Veuillez entrer  l'adresse au format binaire svp: "))

        var = conv_ent(add_binaire)
        print()
        print("\n")
        print(f"la valeur décimale de votre adresse IPV4 est: {var}")
        print("\n")

    elif chose == 3:
        print("\n")
        print()
        print("A.Pour efectuer une conversion binaire.")

        print("\n")

        print("B.Pour effectuer une conversion décimale.")

        print("\n")

        opera = input("Entrez le choix de votre opération par ici: ")
        print("\n")

        opera = opera.upper()

        essai = True

        while essai:

            try:

                opera = str(opera)

            except ValueError:

                print("\n")
                print("Le type de valeur entrée n'est pas correcte!")

                essai = True

                continue

            if opera == "A":
                
                print("\n")

                repertoi_get = input("Entrez le nom du répertoire contenant le fichier à traiter par ici: ")

                print("\n")

                file_name = input("Entrez le nom du ficher à traiter par ici: ")

                liste_ip = get_file(file_name, repertoi_get)

                ipv4_liste = ip_filecalcule_bits(*liste_ip)

                print("\n")

                deci = input("Voulez-vous enrégitrer le resultat dans un ficheier?(o/n) avec o pour oui et n pour non: ")
                print("\n")

                if deci.lower() == "o":

                    print("\n")
                    repert = input("Entrez le nom du répertoire qui devra contenir le fichier: ")

                    print("\n")

                    file = input("Donnez un nom à votre fichier: ")

                    for bit in ipv4_liste:

                        register(file,repert,bit)
                elif deci.lower() == "n":

                    for bit in ipv4_liste:

                        print(bit, end="")
                        print("\n")
                    
                    print()
                essai = False


            if opera == "B":
                
                print("\n")

                repertoi_get = input("Entrez le nom du répertoire contenant le fichier à traiter par ici: ")

                print("\n")

                file_name = input("Entrez le nom du ficher à traiter par ici: ")

                liste_ip = get_file(file_name, repertoi_get)

                ipv4_liste = ip_filecalcule_dec(*liste_ip)

                print("\n")

                deci = input("Voulez-vous enrégitrer le resultat dans un ficheier?(o/n) avec o pour oui et n pour non: ")
                print("\n")

                if deci.lower() == "o":

                    print("\n")
                    repert = input("Entrez le nom du répertoire qui devra contenir le fichier: ")

                    print("\n")

                    file = input("Donnez un nom à votre fichier: ")

                    for bit in ipv4_liste:

                        register(file,repert,bit)
                elif deci.lower() == "n":

                    for bit in ipv4_liste:

                        print(bit, end="")
                        print("\n")
                    
                    print()
                essai = False
    

    elif chose == 0:

        print()
        print()
        print("nous vous remercier d'avoir utilisé notre programme!")
        print()
        print("Bye!")
        continuer = False


   