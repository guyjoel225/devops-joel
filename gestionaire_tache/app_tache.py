from fonctions_gestion import *

continuer = True




while continuer:

    print("\n")
    print("\n")

    print("___________________MENU___________________".center(150))

    print("\n")

    print("1. Ajouter une tâche: titre, description, échéance, statut (à faire/en cours/terminée).")
    print("\n")
    print("2. Afficher les tâches : Filtrer par statut, trier par échéance.")
    print("\n")
    print("3. Mettre à jour une tâche: Modifier la description, le statut, l’échéance.")
    print("\n")
    print("4. Supprimer une tâche.")
    print("\n")
    print("5 Quiter le programme")
    print("\n")
    choice = input("Entrez le choix par ici: ")
    print("\n")
    try:

        choice = int(choice)

    except ValueError:

        print("cette rubrique n'existe pas!")
        print()
        continue

    if choice == 1:

            print("\n")
            titre = input("Entrez le titre de la tache: ")
            print("\n")
            description = input("Entrez la description de la tache: ")
            print("\n")
            echeance = input("Entrez l'échéance de la tache(JJ/MM/AAAA): ")

            print("\n")

            status = input("Entrez le status de la tache(à faire/en cours/terminéé): ")

            print("\n")
            
            tasks = add_task(titre,description,echeance,status)
            
            save = input("voulez-vous sauvegarder la tache?(o'oui'/n'non'): ")

            if save.lower() == "o" or save.lower() == "oui":

                task_save(tasks)

                print("sauvegarde reuissie!!")

            elif save.lower() == "n" or save.lower() == "non":

                print("nous quittons sans une sauvegarde!")

            else:

                print("désolé, aucune action correspondante.")


    elif choice == 2:
        
        valeur = input("Effectuez une recherche à partie de l'échéance ou du status: ")

        afficher(valeur)

    elif choice == 3:
        
        print("Mise des paramètres de la tache.")

        update_task()

    elif choice == 4:
        
        print("Effecter une Suppression de taches!")

        id = input("Entrez l'id de la tache à supprimer de la liste: ")

        tasks = supprimer(id)

        print("\n")

        save = input("voulez-vous enrégistrer la modification?(o/n): ")

        if save.lower() == "o":
             
             task_save(tasks)

        elif save.lower() == "n":

             print("la modification ne sera pas enregistée!")             

    elif choice == 5:
            
            continuer = False

    
    else:
        
        print("ne correspond à aucune action disponible!")

        continuer = True
