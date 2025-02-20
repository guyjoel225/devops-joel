from fonction_ip import *

continuer = True


while continuer:

    # appel de la fonction menu

    print()
    print()
    menu()

    print()

    chose = input("Entrez un choix d'Opération svp!: ")

    try:

        chose = int(chose)
    
    except ValueError:

        continuer = True

        continue

    if chose == 1:

        print()
        print()

        print("Vous avez opté pour une conversion decimale: ")

        print()

        #appel de la fonction conv_binaire

        Add_decimale = str(input("Veuillez entrez votre adresse Ip ici: "))

        var = conv_binaire(Add_decimale)
        print()
        print()

        print(f"La valeur binaire de votre adresse est: {var}")
    
    elif chose == 2:

        print()
        print()

        print("Vous avez opté pour une conversion decimale: ")

        print()

        #appel de la fonction conv_ent

        add_binaire = str(input("Veuillez entrer  l'adresse au format binaire svp: "))

        var = conv_ent(add_binaire)
        print()
        print()
        print(f"la valeur décimale de votre adresse IPV4 est: {var}")
    
    elif chose == 0:

        print()
        print()
        print("nous vous remercier d'avoir utilisé notre programme!")
        print()
        print("Bye!")
        continuer = False


   